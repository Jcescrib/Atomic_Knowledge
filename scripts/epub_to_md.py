#!/usr/bin/env python3
# scripts/epub_to_md.py — Convert an EPUB to clean markdown + extracted images.
#
# Usage:
#     python epub_to_md.py <epub_path> <dest_dir>
#
# Produces (mirroring what MinerU does for PDFs):
#     <dest_dir>/<slug>.md         where <slug> = basename(<dest_dir>)
#     <dest_dir>/images/<file>     every embedded image, flat
#
# Image references in the markdown are rewritten to the flat form
# `images/<filename>`, so the rest of the pipeline (image classification,
# ingest, dedup, integration) treats an EPUB source exactly like a PDF or a
# pre-converted markdown.
#
# Dependencies: ebooklib + beautifulsoup4 (BeautifulSoup). The .docx path used
# python-docx the same way; this is the EPUB analogue.

import os
import sys
import posixpath
import warnings

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# ebooklib emits noisy FutureWarnings about ignored arguments on some versions.
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="ebooklib")


# ─── HTML → markdown ──────────────────────────────────────────────────────────

INLINE_SKIP = {"script", "style", "head", "title", "meta", "link"}


def _esc(text):
    # Escape the markdown structural characters that would otherwise be
    # interpreted. Keep it light — over-escaping hurts readability and the
    # downstream ingest reads prose, not a strict markdown parser.
    return text.replace("\\", "\\\\").replace("`", "\\`")


def _inline(node, images_seen):
    """Render inline content of a node to a markdown string."""
    from bs4 import NavigableString, Tag

    out = []
    for child in node.children:
        if isinstance(child, NavigableString):
            out.append(_esc(str(child)))
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()
        if name in INLINE_SKIP:
            continue
        if name in ("strong", "b"):
            inner = _inline(child, images_seen).strip()
            out.append(f"**{inner}**" if inner else "")
        elif name in ("em", "i"):
            inner = _inline(child, images_seen).strip()
            out.append(f"*{inner}*" if inner else "")
        elif name in ("code", "tt"):
            inner = _inline(child, images_seen).strip()
            out.append(f"`{inner}`" if inner else "")
        elif name == "a":
            inner = _inline(child, images_seen).strip()
            href = child.get("href", "").strip()
            # Drop internal anchors / empty hrefs — keep just the text.
            if href and not href.startswith("#") and inner:
                out.append(f"[{inner}]({href})")
            else:
                out.append(inner)
        elif name == "img":
            out.append(_img_ref(child, images_seen))
        elif name == "br":
            out.append("  \n")
        else:
            # span, sup, sub, abbr, font, etc. — keep the inner text.
            out.append(_inline(child, images_seen))
    return "".join(out)


def _img_ref(tag, images_seen):
    """Render an <img> as a markdown image ref using the flat images/ path."""
    src = (tag.get("src") or tag.get("xlink:href") or "").strip()
    alt = (tag.get("alt") or "").strip()
    if not src:
        return ""
    fname = posixpath.basename(src.split("?")[0])
    images_seen.add(fname)
    return f"![{alt}](images/{fname})"


def _block(node, images_seen, out_lines):
    """Render a block-level node, appending markdown lines to out_lines."""
    from bs4 import NavigableString, Tag

    if isinstance(node, NavigableString):
        text = str(node).strip()
        if text:
            out_lines.append(_esc(text))
        return
    if not isinstance(node, Tag):
        return

    name = node.name.lower()
    if name in INLINE_SKIP:
        return

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = _inline(node, images_seen).strip()
        if text:
            out_lines.append("#" * level + " " + text)
            out_lines.append("")
    elif name == "p":
        text = _inline(node, images_seen).strip()
        if text:
            out_lines.append(text)
            out_lines.append("")
    elif name == "blockquote":
        inner = []
        for child in node.children:
            _block(child, images_seen, inner)
        for line in inner:
            out_lines.append(("> " + line) if line else ">")
        out_lines.append("")
    elif name in ("ul", "ol"):
        ordered = name == "ol"
        idx = 1
        for li in node.find_all("li", recursive=False):
            text = _inline(li, images_seen).strip()
            if text:
                prefix = f"{idx}. " if ordered else "- "
                out_lines.append(prefix + text)
                idx += 1
        out_lines.append("")
    elif name in ("pre",):
        text = node.get_text()
        out_lines.append("```")
        out_lines.append(text.rstrip("\n"))
        out_lines.append("```")
        out_lines.append("")
    elif name == "hr":
        out_lines.append("---")
        out_lines.append("")
    elif name == "img":
        ref = _img_ref(node, images_seen)
        if ref:
            out_lines.append(ref)
            out_lines.append("")
    elif name == "table":
        # Keep tables as raw HTML — the pipeline reads inline <table> HTML
        # directly during ingest, exactly as it does for MinerU output.
        out_lines.append(str(node))
        out_lines.append("")
    elif name in ("body", "html", "div", "section", "article", "main",
                  "header", "footer", "figure", "figcaption", "nav"):
        for child in node.children:
            _block(child, images_seen, out_lines)
    else:
        # Unknown block container — recurse so nothing is silently dropped.
        for child in node.children:
            _block(child, images_seen, out_lines)


def html_to_markdown(html, images_seen):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body or soup
    out_lines = []
    for child in body.children:
        _block(child, images_seen, out_lines)
    # Collapse runs of >1 blank line.
    cleaned = []
    blank = False
    for line in out_lines:
        if line.strip() == "":
            if blank:
                continue
            blank = True
        else:
            blank = False
        cleaned.append(line)
    return "\n".join(cleaned).strip()


# ─── EPUB driver ────────────────────────────────────────────────────────────

def convert(epub_path, dest_dir):
    slug = os.path.basename(os.path.normpath(dest_dir))
    md_path = os.path.join(dest_dir, slug + ".md")
    images_dir = os.path.join(dest_dir, "images")
    os.makedirs(dest_dir, exist_ok=True)

    book = epub.read_epub(epub_path)

    # Title for the document H1 (fall back to the slug).
    title = slug
    md_titles = book.get_metadata("DC", "title")
    if md_titles and md_titles[0] and md_titles[0][0]:
        title = md_titles[0][0].strip()

    images_seen = set()
    sections = []

    # Iterate documents in spine order so chapters stay in reading order.
    spine_ids = [item[0] for item in book.spine]
    docs = {}
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        docs[item.get_id()] = item

    ordered = [docs[i] for i in spine_ids if i in docs]
    # Append any document not referenced by the spine, just in case.
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        if item not in ordered:
            ordered.append(item)

    for item in ordered:
        # Skip the EPUB navigation / TOC document — it carries no content,
        # only a table-of-contents list that would be noise for the ingest.
        if isinstance(item, epub.EpubNav):
            continue
        props = item.get_name(), " ".join(getattr(item, "properties", []) or [])
        if "nav" in props[1].split():
            continue
        try:
            html = item.get_content().decode("utf-8", errors="replace")
        except Exception:
            continue
        md = html_to_markdown(html, images_seen)
        if md.strip():
            sections.append(md)

    # Extract embedded images (flat) — mirror MinerU's images/ layout.
    extracted = 0
    image_items = list(book.get_items_of_type(ebooklib.ITEM_IMAGE))
    # Some covers are typed as ITEM_COVER rather than ITEM_IMAGE.
    image_items += list(book.get_items_of_type(ebooklib.ITEM_COVER))
    if image_items:
        os.makedirs(images_dir, exist_ok=True)
    for item in image_items:
        fname = posixpath.basename(item.get_name())
        if not fname:
            continue
        with open(os.path.join(images_dir, fname), "wb") as fh:
            fh.write(item.get_content())
        extracted += 1

    body = "\n\n".join(sections)
    document = f"# {title}\n\n{body}\n" if body else f"# {title}\n"

    with open(md_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(document)

    # Report to stderr (the destination path goes to stdout, like pipeline.sh).
    print(
        f"[epub] {len(sections)} section(s), {extracted} image(s) extracted, "
        f"{len(images_seen)} image ref(s) in markdown",
        file=sys.stderr,
    )
    return md_path


def main(argv):
    if len(argv) != 3:
        print("Usage: epub_to_md.py <epub_path> <dest_dir>", file=sys.stderr)
        return 1
    epub_path, dest_dir = argv[1], argv[2]
    if not os.path.isfile(epub_path):
        print(f"ERROR: not a file: {epub_path}", file=sys.stderr)
        return 1
    convert(epub_path, dest_dir)
    print(dest_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

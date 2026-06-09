# -*- coding: utf-8 -*-
import json, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ps = sorted(glob.glob(os.path.join(ROOT, "outputs", "bridges", "batch*.json")))
ps = [p.replace("\\", "/") for p in ps]
open(os.path.join(ROOT, "outputs", "bridges", "_paths.json"), "w").write(json.dumps(ps))
print(len(ps)); print(ps[0]); print(ps[-1])

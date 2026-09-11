# -*- coding: utf-8 -*-
"""Build the offline, self-contained 2026 汉字大赛备赛营 HTML.

Injects into tool/index.template.html:
  /*__LIB__*/      <- vendor/hanzi-writer.min.js
  /*__DATA__*/     <- data/dasai_data.json     (cycles x categories x entries)
  /*__CHARDATA__*/ <- data/chardata.json        (stroke + median data)

Writes index.html at the repo root (what Vercel serves) and an OneDrive
offline copy. Run:  python build.py
"""
import json, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
ONEDRIVE = r"C:/Users/zhouf/OneDrive/chinese teaching resources/2026汉字大赛备赛营"
TARGETS = [P("index.html"), os.path.join(ONEDRIVE, "2026汉字大赛备赛营.html")]

data = json.load(open(P("data", "dasai_data.json"), encoding="utf-8"))
chardata = json.load(open(P("data", "chardata.json"), encoding="utf-8"))
lib = open(P("vendor", "hanzi-writer.min.js"), encoding="utf-8").read().replace("</script", "<\\/script")
tpl = open(P("tool", "index.template.html"), encoding="utf-8").read()

out = (tpl
       .replace("/*__LIB__*/", lib)
       .replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
       .replace("/*__CHARDATA__*/{}", json.dumps(chardata, ensure_ascii=False, separators=(",", ":"))))
for ph in ("/*__LIB__*/", "/*__DATA__*/", "/*__CHARDATA__*/"):
    assert ph not in out, "placeholder not filled: " + ph

with open(P("tool", "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
copied = []
for t in TARGETS:
    parent = os.path.dirname(t)
    if not os.path.isdir(parent):
        if parent.replace("\\", "/").startswith("C:/Users/zhouf/OneDrive"):
            os.makedirs(parent, exist_ok=True)
        else:
            continue
    shutil.copy(P("tool", "index.html"), t)
    copied.append(t)

n = sum(len(v[k]) for v in data["cycles"].values() for k in ("base", "read", "write"))
print("built %.2f MB | %d entries | %d chars" % (len(out.encode("utf-8")) / 1048576, n, len(chardata)))
for t in copied:
    print("  " + t)

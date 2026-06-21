#!/usr/bin/env python3
# Sort manifest.json files[] by projectID, and modlist.html <li>s by anchor text.
import json, re
from pathlib import Path

here = Path(__file__).parent

# manifest.json: stable numeric sort, keep the 2-space indent (no trailing newline in original).
m = here / "manifest.json"
data = json.loads(m.read_text(encoding="utf-8"))
data["files"].sort(key=lambda f: f["projectID"])
m.write_text(json.dumps(data, indent=2), encoding="utf-8")

# modlist.html: sort <li> lines by the <a> text (case-insensitive). Keep BOM + <ul> wrapper.
# assumes one <li> per line, which is how the file is generated.
h = here / "modlist.html"
li = [l for l in h.read_text(encoding="utf-8-sig").splitlines() if l.lstrip().startswith("<li>")]
li.sort(key=lambda l: re.search(r"<a[^>]*>(.*?)</a>", l).group(1).casefold())
h.write_text("﻿<ul>\n" + "\n".join(li) + "\n</ul>\n", encoding="utf-8")

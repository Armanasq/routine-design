#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "papers" / "catalog.json").read_text())
papers = data["papers"]
assert len({p["id"] for p in papers}) == len(papers)
errors = []
for paper in papers:
    for key in ("review", "source"):
        path = root / paper[key]
        if not path.is_file():
            errors.append(f"{paper['id']}: missing {key}: {path}")
    if paper["local_full_text"] and not paper["license_verified"]:
        errors.append(f"{paper['id']}: full-text marked local without verified redistribution license")
    if not paper["url"].startswith("https://"):
        errors.append(f"{paper['id']}: invalid URL")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(papers)} unique papers with review/source records.")

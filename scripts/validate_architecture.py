#!/usr/bin/env python3
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
paths=["research/knowledge-map.json","papers/catalog.json"]
paths += [str(p.relative_to(root)) for p in (root/"schemas").glob("*.json")]
paths += [str(p.relative_to(root)) for p in (root/"tests/scenarios").glob("*.json")]
for path in paths:
    with (root/path).open(encoding="utf-8") as f:
        json.load(f)
map_obj=json.loads((root/"research/knowledge-map.json").read_text())
ids={p["id"] for p in json.loads((root/"papers/catalog.json").read_text())["papers"]}
for mechanism in map_obj["mechanisms"]:
    assert set(mechanism["papers"])<=ids,mechanism["id"]
    assert len(mechanism["papers"])>=2,mechanism["id"]
print(f"Validated {len(paths)} JSON files and {len(map_obj['mechanisms'])} source-connected mechanisms.")

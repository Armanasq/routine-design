#!/usr/bin/env python3
import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--paper-id", required=True)
parser.add_argument("--url", required=True)
parser.add_argument("--license-url", required=True)
parser.add_argument("--format", choices=["pdf", "tex", "html"], default="pdf")
parser.add_argument("--max-bytes", type=int, default=30_000_000)
args = parser.parse_args()
catalog = json.loads((root / "papers" / "catalog.json").read_text())["papers"]
paper = next((x for x in catalog if x["id"] == args.paper_id), None)
if paper is None:
    parser.error("Unknown paper id")
if not args.url.startswith("https://") or not args.license_url.startswith("https://"):
    parser.error("HTTPS source and redistribution license URLs required")
print("Before continuing, verify license permits redistribution in a PUBLIC repository.")
confirm = input("Have you reviewed both the article license and this exact source version? Type YES: ")
if confirm != "YES":
    raise SystemExit("Not downloaded")
request = urllib.request.Request(args.url, headers={"User-Agent": "RoutinResearch/1.0"})
with urllib.request.urlopen(request, timeout=30) as response:
    size = response.headers.get("Content-Length")
    if size and int(size) > args.max_bytes:
        raise SystemExit("File too large")
    payload = response.read(args.max_bytes + 1)
if len(payload) > args.max_bytes:
    raise SystemExit("File too large")
path = root / paper["source"]
target = path.parent / ("paper." + args.format)
target.write_bytes(payload)
metadata = {"paper_id": args.paper_id, "source_url": args.url, "license_url": args.license_url, "fetched_utc": datetime.now(timezone.utc).isoformat(), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(), "format": args.format, "manual_rights_confirmation": True}
(target.parent / "ACQUISITION.json").write_text(json.dumps(metadata, indent=2) + "\n")
print("Saved", target)

#!/usr/bin/env python3
"""Validate incidents, taxonomy and example traces.

Usage:  python scripts/validate.py [incidents_dir]
Exit code 0 = everything valid, 1 = at least one problem.
Requires: jsonschema, PyYAML (see scripts/requirements.txt).
"""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
errors = []


class NoDateLoader(yaml.SafeLoader):
    """SafeLoader that keeps ISO dates as plain strings (the schema expects strings)."""


NoDateLoader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, Loader=NoDateLoader)


def err(msg):
    errors.append(msg)
    print("ERROR:", msg)


def schema_errors(validator, doc, label):
    for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        err(f"{label}: {loc}: {e.message}")


def main():
    inc_schema = json.loads((ROOT / "schema/incident.schema.json").read_text())
    trace_schema = json.loads((ROOT / "schema/trace.schema.json").read_text())
    Draft202012Validator.check_schema(inc_schema)
    Draft202012Validator.check_schema(trace_schema)
    inc_v = Draft202012Validator(inc_schema, format_checker=FormatChecker())
    trace_v = Draft202012Validator(trace_schema, format_checker=FormatChecker())

    # Taxonomy
    tax = load_yaml(ROOT / "taxonomy/failure-modes.yaml")
    modes = {m["id"]: m for m in tax["failure_modes"]}
    if len(modes) != len(tax["failure_modes"]):
        err("taxonomy: duplicate failure mode ids")
    for m in modes.values():
        for k in ("name", "definition", "example", "detection_eval_idea", "typical_loss_types", "example_incidents"):
            if k not in m or (k != "example_incidents" and m[k] in (None, "", [])):
                err(f"taxonomy: {m.get('id')}: missing '{k}'")

    # Incidents
    inc_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "incidents"
    files = sorted(inc_dir.glob("*.yaml"))
    ids = {}
    for p in files:
        doc = load_yaml(p)
        label = p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else str(p)
        if not isinstance(doc, dict):
            err(f"{label}: not a mapping")
            continue
        schema_errors(inc_v, doc, label)
        iid = doc.get("id")
        if iid != p.stem:
            err(f"{label}: id '{iid}' must equal file name '{p.stem}'")
        if iid in ids:
            err(f"{label}: duplicate id {iid}")
        ids[iid] = doc
        # date vs precision
        d, prec = doc.get("date", ""), doc.get("date_precision")
        want = {"year": 4, "month": 7, "day": 10}.get(prec)
        if want and len(d) != want:
            err(f"{label}: date '{d}' does not match date_precision '{prec}'")
        if isinstance(iid, str) and d and not iid.startswith(d[:7]):
            err(f"{label}: id prefix should match date year-month ({d[:7]})")
        for fm in doc.get("failure_modes", []):
            if fm not in modes:
                err(f"{label}: unknown failure mode '{fm}'")
        urls = [s.get("url") for s in doc.get("source_urls", [])]
        if len(urls) != len(set(urls)):
            err(f"{label}: duplicate source URLs")
        primary_types = ("court_or_regulator", "company")
        if doc.get("category") == "research_finding":
            primary_types += ("research",)
        if doc.get("verification_status", "").startswith("verified_primary") and not any(
            s.get("source_type") in primary_types for s in doc.get("source_urls", [])
        ):
            err(f"{label}: verified_primary requires a {' or '.join(primary_types)} source")
        if doc.get("verification_status") == "verified_multiple_secondary" and len(urls) < 2:
            err(f"{label}: verified_multiple_secondary needs at least 2 sources")
        for fld in ("summary", "what_happened"):
            if re.search(r"\s(\u201c|\")[^\u201d\"]{200,}", doc.get(fld, "")):
                err(f"{label}: {fld} contains a long quotation; summaries must be our own words")

    # Taxonomy <-> incident cross-check (both directions)
    for mid, m in modes.items():
        listed = set(m.get("example_incidents") or [])
        actual = {i for i, d in ids.items() if mid in d.get("failure_modes", [])}
        if listed != actual:
            err(f"taxonomy: {mid}: example_incidents {sorted(listed)} != incidents tagged {sorted(actual)}")

    # Traces
    n_traces = 0
    for p in sorted((ROOT / "traces").rglob("*.jsonl")):
        for ln, line in enumerate(p.read_text().splitlines(), 1):
            if not line.strip():
                continue
            label = f"{p.relative_to(ROOT).as_posix()}:{ln}"
            try:
                t = json.loads(line)
            except json.JSONDecodeError as e:
                err(f"{label}: invalid JSON: {e}")
                continue
            n_traces += 1
            schema_errors(trace_v, t, label)
            if t.get("incident_id") is not None and t["incident_id"] not in ids:
                err(f"{label}: unknown incident_id '{t['incident_id']}'")
            if t.get("failure_mode") not in modes:
                err(f"{label}: unknown failure_mode '{t.get('failure_mode')}'")

    print(f"Checked {len(files)} incidents, {len(modes)} failure modes, {n_traces} traces.")
    if errors:
        print(f"FAILED with {len(errors)} problem(s).")
        return 1
    print("OK: all entries validate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

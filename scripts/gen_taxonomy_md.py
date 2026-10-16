#!/usr/bin/env python3
"""Generate taxonomy/failure-modes.md from taxonomy/failure-modes.yaml (+ incident titles)."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent


class L(yaml.SafeLoader):
    pass


L.yaml_implicit_resolvers = {
    k: [(t, r) for t, r in v if t != "tag:yaml.org,2002:timestamp"] for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}

tax = yaml.load((ROOT / "taxonomy/failure-modes.yaml").read_text(), Loader=L)
titles = {p.stem: yaml.load(p.read_text(), Loader=L)["title"] for p in (ROOT / "incidents").glob("*.yaml")}

out = [
    "# Failure-mode taxonomy",
    "",
    "<!-- GENERATED from failure-modes.yaml by scripts/gen_taxonomy_md.py. Do not edit by hand. -->",
    "",
    "Fourteen failure modes used to tag incidents (`failure_modes` in `incidents/*.yaml`) and traces. "
    "The machine-readable source of truth is [`failure-modes.yaml`](failure-modes.yaml). "
    "A mode with no linked incident is a known pattern we have not yet verified against a public incident; "
    "its example is marked *Illustrative* where it is not drawn from a catalogued entry.",
    "",
    "| id | mode | group | linked incidents |",
    "|---|---|---|---|",
]
for m in tax["failure_modes"]:
    out.append(f"| `{m['id']}` | {m['name']} | {m['group']} | {len(m['example_incidents'])} |")
out.append("")
for m in tax["failure_modes"]:
    out += [
        f"## {m['name']}",
        "",
        f"`{m['id']}` · group: {m['group']}",
        "",
        f"**Definition.** {m['definition']}",
        "",
        f"**Example.** {m['example']}",
        "",
        f"**Detection / eval idea.** {m['detection_eval_idea']}",
        "",
        "**Typical loss types.** " + ", ".join(f"`{t}`" for t in m["typical_loss_types"]),
        "",
        "**Example incidents.**",
    ]
    if m["example_incidents"]:
        for i in m["example_incidents"]:
            out.append(f"- [`{i}`](../incidents/{i}.yaml): {titles[i]}")
    else:
        out.append("- None catalogued yet (see roadmap in the top-level README).")
    out.append("")
(ROOT / "taxonomy/failure-modes.md").write_text("\n".join(out))
print("wrote taxonomy/failure-modes.md")

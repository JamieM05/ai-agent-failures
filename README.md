# ai-agent-failures

A curated, comprehensive database of known AI and agent failures: every known failure mode, incident and trace we can verify from public sources.

It is the seed corpus for an **agent-failure eval and insurance data business**: a structured, source-linked record of how AI systems and autonomous agents go wrong, what it cost, and how it could have been detected.

> **Status: early seed (v0.1).** 12 verified incidents, a 14-mode taxonomy, schemas, a validator, and pointers to public trace datasets. See [Status and roadmap](#status-and-roadmap).

## Purpose

- **Evals:** turn real failures into repeatable tests. Each failure mode in [`taxonomy/`](taxonomy/failure-modes.md) carries a detection/eval idea, and [`traces/`](traces/README.md) defines a format for step-level agent traces.
- **Insurance and risk data:** give underwriters and risk teams consistent fields for severity, harm type, loss estimate (with basis and confidence), outcome and root cause, each tied to public sources.
- **A shared vocabulary:** one failure-mode taxonomy used across incidents, traces and evals.

## Repository layout

```
README.md                 this file
LICENSE                   MIT (code and curation)
CONTRIBUTING.md           how to add or correct an entry
incidents/                one YAML file per incident + incidents/README.md (index, omitted candidates)
taxonomy/                 failure-modes.yaml (source of truth) and failure-modes.md (generated)
traces/                   JSONL trace format, a synthetic example, and pointers to public trace sets
schema/                   incident.schema.json, trace.schema.json, and schema/README.md (severity scale etc.)
scripts/                  validate.py (jsonschema + PyYAML), gen_taxonomy_md.py
.github/ISSUE_TEMPLATE/   new-incident issue template
```

## Entry schema (summary)

Each file in `incidents/` is one YAML record validated against [`schema/incident.schema.json`](schema/incident.schema.json). Key fields:

| field | meaning |
|---|---|
| `id`, `title`, `date`, `date_precision` | stable slug (`YYYY-MM-name`), headline, and date with its precision (year / month / day) |
| `category` | `ai_incident`, `precedent_ml` (non-agentic ML) or `precedent_non_ai` (conventional software kept as an analogy) |
| `model_or_agent`, `vendor_or_deployer`, `sector` | what failed and who deployed it |
| `summary`, `what_happened` | short factual descriptions **in our own words** |
| `failure_modes[]` | ids from the taxonomy |
| `severity` (1-5), `harm_types[]` | rubric in [`schema/README.md`](schema/README.md) |
| `loss_estimate` (optional) | `amount`, `currency`, `basis`, `confidence` |
| `outcome`, `root_cause` | what happened next, and who established the cause (court/regulator, vendor, third party) |
| `source_urls[]` | each with title, publisher, type and `accessed` date |
| `verification_status`, `notes`, `contributor` | provenance |

Run `pip install -r scripts/requirements.txt && python scripts/validate.py` to check everything.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: open an issue with the new-incident template or a pull request adding one YAML file, with real sources, our-own-words text, and a passing `scripts/validate.py`.

## Verifiability rule

**Every entry must be verifiable from public sources.** If a claim cannot be traced to a linked public source (court record, regulator or company statement, research paper, or reputable reporting), it does not go in. Rumours, anecdotes and "someone told me" incidents are listed as omitted candidates in [`incidents/README.md`](incidents/README.md), not as entries. Where the only source is the affected party's own account, or a page we could not read in full, the entry says so in `notes` and uses a weaker `verification_status`.

## Licence note

- **Code and curation** (scripts, schemas, taxonomy, structure, our summaries and annotations) are released under the [MIT licence](LICENSE).
- **Source articles remain the property of their publishers.** Entries link to sources and contain only short factual summaries in our own words. Report text is not copied here; please do not add it.
- **Third-party trace datasets** referenced in [`traces/README.md`](traces/README.md) keep their own licences. We link to them; we do not redistribute them.

## Status and roadmap

**Now (v0.1):** 12 incidents (10 `ai_incident` entries, one of which is a security-vulnerability disclosure with no known in-the-wild exploitation; 1 `precedent_ml`; 1 `precedent_non_ai`), 14 failure modes, schemas, validator.

**Next:**
- Cover the failure modes that currently have no verified incident: reward hacking / specification gaming, privacy leaks, multi-agent coordination failure.
- Add more verified incidents per mode, especially agentic ones with quantified losses.
- Import and normalise a small sample of public traces into `traces/` (respecting their licences) and link them to incidents.
- Add automated link-checking and a CI workflow running `scripts/validate.py`.
- Add loss-estimate guidance for insurance use (basis conventions, currency normalisation).

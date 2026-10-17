# Schema

- [`incident.schema.json`](incident.schema.json): JSON Schema (draft 2020-12) for files in `incidents/*.yaml`.
- [`trace.schema.json`](trace.schema.json): JSON Schema for one line of a trace `.jsonl` file (see [`../traces/README.md`](../traces/README.md)).

`scripts/validate.py` checks these schemas plus extra rules the schema cannot express (id equals file name, date precision, failure-mode ids exist in the taxonomy, taxonomy and incident links agree, source-count rules).

## Incident fields

| field | required | notes |
|---|---|---|
| `id` | yes | `YYYY-MM-slug`; equals file name |
| `title` | yes | headline |
| `date`, `date_precision` | yes | `YYYY`, `YYYY-MM` or `YYYY-MM-DD`, matched by `year`/`month`/`day`. Use the incident date, or first public report if the incident date is unknown |
| `category` | yes | `ai_incident`, `research_finding`, `precedent_ml`, `precedent_non_ai` (see below) |
| `model_or_agent`, `vendor_or_deployer`, `sector` | yes | `sector` is a free-form snake_case label |
| `summary` | yes | 1-3 sentences, our own words |
| `what_happened` | yes | factual narrative, our own words |
| `failure_modes[]` | yes | taxonomy ids |
| `severity` | yes | 1-5, see below |
| `harm_types[]` | yes | financial_loss, data_loss, privacy_breach, security_exposure, reputational, legal_liability, regulatory_action, consumer_harm, physical_safety, market_disruption, operational_disruption, misinformation, no_realised_harm (research findings only) |
| `loss_estimate` | no | `amount`, `currency` (ISO 4217), `basis`, `confidence` (high / medium / low) |
| `outcome` | yes | `types[]` (enum) and `description` |
| `root_cause` | yes | `attribution` (`court_or_regulator_finding`, `vendor_stated`, `third_party_analysis`, `unknown`) and `description` |
| `source_urls[]` | yes | each: `url`, `title`, `publisher`, `source_type`, `accessed` (YYYY-MM-DD), optional `note` |
| `verification_status` | yes | see below |
| `notes` | no | caveats and context |
| `contributor` | yes | who added it |

### Research findings

`research_finding` covers behaviour observed in a controlled setting (an evaluation, red-team exercise, training run or research environment) and published by the lab or researchers, such as a model deceiving an evaluator, gaming its reward, or resisting shutdown in a test. These matter for evals even when nobody was harmed. Rules:

- `severity` rates realised impact, so a research finding is normally `1`; use more only if the behaviour caused real-world loss.
- Use `harm_types: [no_realised_harm]` unless real harm occurred.
- Use `outcome.types` such as `research_published` or `mitigation_published` (for example a system card noting a training fix).
- The original publication is the primary source: a lab's own system card or blog post is `company`, a paper is `research`. For `research_finding` entries, `verified_primary` needs at least one `company` or `research` source that was read in full. Press coverage alone gives the secondary levels.
- Say in `notes` whether the setup was designed to elicit the behaviour (for example an artificial scenario with a planted goal conflict) and how often it occurred. Do not overstate prevalence.

### Severity scale (1-5)

Severity rates the **realised or officially established impact** of the incident, not the worst case that could have happened. For a vulnerability disclosed with no known exploitation, cap at 3.

| level | label | meaning |
|---|---|---|
| 1 | Minor | Embarrassing or trivial; no real loss, no one relied on the output. Quickly removed or fixed. |
| 2 | Moderate | Public reputational damage, user confusion or a feature withdrawn; no significant quantified loss or liability. |
| 3 | Significant | Concrete harm to a person or organisation: a legal ruling or sanction, data loss (recoverable), compensation, or low-to-mid six-figure cost. |
| 4 | Major | Large financial loss (roughly USD 1m-100m), significant regulatory action, or unrecovered large-scale data or privacy harm. |
| 5 | Severe | Extreme impact: loss above roughly USD 100m, threat to a firm's survival, systemic market disruption, or loss of life / serious physical injury. |

### Verification status

| value | meaning |
|---|---|
| `verified_primary` | A primary source (court record, regulator document, or the deployer's own statement) was read and supports the core facts. Needs at least one `court_or_regulator` or `company` source. |
| `verified_multiple_secondary` | Two or more independent reputable secondary sources support the core facts; no primary source (or the primary source is only the deployer's own brief statement). |
| `verified_single_secondary` | One reputable source supports the core facts. Treat as provisional. |
| `unverified` | Reserved for drafts; not accepted into the main set. |

A source marked in `notes` or the source `note` as "not machine-read" was identified through search results rather than read in full; the entry's facts must still be supported by sources that were read.

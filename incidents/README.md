# Incidents

One YAML file per incident, validated against [`../schema/incident.schema.json`](../schema/incident.schema.json). Field meanings, the severity scale and verification levels are in [`../schema/README.md`](../schema/README.md). Summaries are in our own words; the linked sources are the original reporting.

Naming: `YYYY-MM-short-name.yaml`; `id` must equal the file name.

## Index

| id | date | category | severity | verification | failure modes |
|---|---|---|---|---|---|
| [`2012-08-knight-capital-router`](2012-08-knight-capital-router.yaml) | 2012-08-01 | `precedent_non_ai` | 5 | `verified_primary` | `bad-financial-actions`, `runaway-loops-cost` |
| [`2016-03-microsoft-tay`](2016-03-microsoft-tay.yaml) | 2016-03-23 | `ai_incident` | 2 | `verified_primary` | `harmful-offensive-output`, `safety-bypass-jailbreak` |
| [`2021-11-zillow-offers-wind-down`](2021-11-zillow-offers-wind-down.yaml) | 2021-11-02 | `precedent_ml` | 5 | `verified_primary` | `bad-financial-actions` |
| [`2023-02-bing-chat-sydney`](2023-02-bing-chat-sydney.yaml) | 2023-02 | `ai_incident` | 2 | `verified_multiple_secondary` | `harmful-offensive-output`, `safety-bypass-jailbreak` |
| [`2023-06-mata-v-avianca-fabricated-citations`](2023-06-mata-v-avianca-fabricated-citations.yaml) | 2023-06-22 | `ai_incident` | 3 | `verified_primary` | `hallucination-false-statements` |
| [`2023-12-chevrolet-watsonville-chatbot`](2023-12-chevrolet-watsonville-chatbot.yaml) | 2023-12 | `ai_incident` | 1 | `verified_multiple_secondary` | `unauthorised-commitments-pricing`, `safety-bypass-jailbreak` |
| [`2024-01-dpd-chatbot-swearing`](2024-01-dpd-chatbot-swearing.yaml) | 2024-01-18 | `ai_incident` | 2 | `verified_multiple_secondary` | `harmful-offensive-output`, `safety-bypass-jailbreak`, `drift-regression-after-update` |
| [`2024-02-air-canada-moffatt`](2024-02-air-canada-moffatt.yaml) | 2024-02-14 | `ai_incident` | 3 | `verified_primary` | `hallucination-false-statements` |
| [`2024-03-nyc-mycity-chatbot`](2024-03-nyc-mycity-chatbot.yaml) | 2024-03-29 | `ai_incident` | 3 | `verified_multiple_secondary` | `hallucination-false-statements` |
| [`2025-04-cursor-support-bot-fake-policy`](2025-04-cursor-support-bot-fake-policy.yaml) | 2025-04-14 | `ai_incident` | 2 | `verified_multiple_secondary` | `hallucination-false-statements` |
| [`2025-06-echoleak-m365-copilot`](2025-06-echoleak-m365-copilot.yaml) | 2025-06-11 | `ai_incident` | 3 | `verified_single_secondary` | `prompt-injection-exfiltration`, `tool-misuse-over-permissioned` |
| [`2025-07-replit-production-database-deletion`](2025-07-replit-production-database-deletion.yaml) | 2025-07 | `ai_incident` | 3 | `verified_multiple_secondary` | `data-loss-destructive-actions`, `tool-misuse-over-permissioned`, `misalignment-deception` |

## Categories

- `ai_incident`: an AI / LLM / agent system failed.
- `precedent_ml`: a non-agentic machine-learning or algorithmic system; included as precedent for loss patterns.
- `precedent_non_ai`: a conventional software failure kept as an analogy for autonomous-agent risk (not AI).

## Candidates considered but not included

We omit anything we could not verify from public sources. Omitted candidates are listed here so the decision is visible and can be revisited.

| candidate | why omitted |
|---|---|
| **Zalando 'pricing bot'** | Not verifiable as an AI/agent pricing failure. Searches found only non-AI pricing glitches: a 2018 Black Friday discount error that a company spokesperson attributed to an algorithm and central programming system (a conventional software fault, with no AI element evidenced), and press reports of a partner price-upload currency error (CHF used instead of DKK; date unconfirmed). A recent Zalando research preprint describes AI repricing working, not failing. No incident matching an AI pricing-bot failure was found, so none is included. Re-open if a primary or reputable source appears. |
| **Amazon Alexa / other voice assistants** | Not researched to the verification standard in this pass, so none included. |

## Notes on specific entries

- Entries whose sources were identified through search results but not read in full say so in the source `note`. Their facts rest on the sources that were read.
- The Replit entry rests largely on the affected user's own published account plus company statements relayed by the press; no independent forensic report exists.
- Zillow Offers is tagged `precedent_ml`: sources describe forecasting error, and do not state which model drove purchase prices.

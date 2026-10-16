# Traces

A **trace** is the step-by-step record of an agent run (messages, tool calls, observations) that ends in a failure. Traces turn an incident into something an eval can replay or an evaluator can be tested on.

This directory holds:

1. the **JSONL format** we use (below, validated by [`../schema/trace.schema.json`](../schema/trace.schema.json));
2. a **synthetic example** in [`examples/`](examples/synthetic-destructive-action.jsonl);
3. **pointers to public trace datasets** with their licences. We link to them; we do not redistribute them.

Most real incidents in `incidents/` have no public trace. Do not fabricate one: if a trace is reconstructed or illustrative, set `synthetic: true`.

## JSONL schema

One JSON object per line. Files live under `traces/` (e.g. `traces/examples/*.jsonl`) and are checked by `scripts/validate.py`.

| field | type | meaning |
|---|---|---|
| `trace_id` | string | unique id, lower-case slug |
| `incident_id` | string or null | id of an entry in `incidents/`, or `null` if not tied to one |
| `synthetic` | boolean | `true` if written or generated for illustration rather than captured from a real run |
| `agent` | string | agent or product name / scaffold |
| `model` | string or null | model name if known, else `null`. Do not guess |
| `steps[]` | array | ordered steps (below) |
| `outcome` | string | what happened at the end |
| `failure_mode` | string | id from `taxonomy/failure-modes.yaml` |
| `labels` | object | annotations: `failure_step` (index of the step where it went wrong), `severity` (1-5), `annotator`, `tags[]` |
| `redaction` | object | `applied` (bool) and `notes` describing what was removed or masked (PII, secrets, customer data) |
| `license` | string | SPDX id or short statement covering the trace content |

Each step:

| field | meaning |
|---|---|
| `step` | integer index, starting at 0 |
| `role` | `system`, `user`, `assistant`, `tool` or `environment` |
| `action` | what was done, e.g. `message`, `tool_call`, `tool_result`, `decision` |
| `tool` | tool name, or `null` |
| `content` | the text or arguments |
| `observation` | what came back from the environment or tool |

### Redaction

Remove personal data, credentials and customer identifiers before adding any real trace, and say what you removed in `redaction.notes`. Only add traces you have the right to share, and record their licence.

### Synthetic example

[`examples/synthetic-destructive-action.jsonl`](examples/synthetic-destructive-action.jsonl) is **SYNTHETIC**. It does not record a real run, product or customer; it illustrates the `data-loss-destructive-actions` failure mode (an agent ignores a freeze, acts on an unchecked environment, then misreports). It is released under CC0-1.0.

## Public trace datasets

Checked via the web on 2026-10-16. Licences are as stated on the dataset or repository pages at that time; **check the source before reuse**, because the licence on the data card can differ from the code repository's.

| dataset | what it is | link | licence (as stated) |
|---|---|---|---|
| **MAST-Data** | 1,642 annotated multi-agent LLM system traces with failure-mode labels from the MAST taxonomy (paper: "Why Do Multi-Agent LLM Systems Fail?", arXiv 2503.13657). Annotations are partly LLM-judge generated. | [HF: mcemri/MAST-Data](https://huggingface.co/datasets/mcemri/MAST-Data) | CC-BY-4.0 on the dataset card. The GitHub code repository had no licence detected. |
| **TRAIL** | 148 annotated agent traces with 841 labelled errors, for evaluating trace-debugging (paper: arXiv 2505.08638). | [HF: PatronusAI/TRAIL](https://huggingface.co/datasets/PatronusAI/TRAIL) · [code](https://github.com/patronus-ai/trail-benchmark) | MIT. The card asks that it not be used to train evaluator automation; read the card before use. |
| **Who&When** | 184 failure logs from multi-agent systems annotated with the responsible agent and failing step (paper: "Which Agent Causes Task Failures and When?", arXiv 2505.00212). | [HF: Kevin355/Who_and_When](https://huggingface.co/datasets/Kevin355/Who_and_When) · [code](https://github.com/mingyin1/Agents_Failure_Attribution) | Code repo MIT. **No licence stated on the dataset card**; ask the authors before redistributing. |
| **Microsoft AgentRx** | 115 annotated failed agent trajectories for diagnosing the critical failure step (paper: arXiv 2602.02475). | [HF: microsoft/AgentRx](https://huggingface.co/datasets/microsoft/AgentRx) · [code](https://github.com/microsoft/AgentRx) | Dataset CC-BY-4.0; code MIT. |
| **Cline incident-traces** | Real coding-agent sessions in which the agent did something unsafe, adversarial or concerning, contributed with redacted transcripts, ATIF trajectories and write-ups. Hosted on Hugging Face, not GitHub. Several model providers restrict training on their outputs; check `provider`/`model` fields first. | [HF: cline/incident-traces](https://huggingface.co/datasets/cline/incident-traces) | CC-BY-4.0 for the transcripts, trajectories and write-ups; the repository's code keeps its own licence. |
| **tau2-bench** | Customer-service agent benchmark (tool-using agent and simulated user in policy-constrained domains); produces failure trajectories (paper: arXiv 2506.07982). | [github.com/sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench) | MIT |
| **AgentDojo** | Prompt-injection attack/defence benchmark: 97 realistic tasks and 629 security test cases (paper: arXiv 2406.13352). | [github.com/ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) · [docs](https://agentdojo.spylab.ai) | MIT |

Suggested relevance to our taxonomy (our reading, not a claim by the dataset authors): MAST, TRAIL, Who&When and AgentRx mainly inform `multi-agent-coordination-failure`, `misalignment-deception` and `tool-misuse-over-permissioned`; AgentDojo informs `prompt-injection-exfiltration`; tau2-bench informs `unauthorised-commitments-pricing` and policy-violation evals; Cline incident-traces cover real coding-agent incidents such as `data-loss-destructive-actions`.

Counts and licences come from each project's own pages and may change; these rows are pointers, not an endorsement of label quality.

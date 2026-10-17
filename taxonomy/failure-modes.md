# Failure-mode taxonomy

<!-- GENERATED from failure-modes.yaml by scripts/gen_taxonomy_md.py. Do not edit by hand. -->

17 failure modes used to tag incidents (`failure_modes` in `incidents/*.yaml`) and traces. The machine-readable source of truth is [`failure-modes.yaml`](failure-modes.yaml). A mode with no linked incident is a known pattern we have not yet verified against a public incident; its example is marked *Illustrative* where it is not drawn from a catalogued entry.

| id | mode | group | linked incidents |
|---|---|---|---|
| `data-loss-destructive-actions` | Data loss / destructive actions | Agent actions | 1 |
| `bad-financial-actions` | Bad financial actions / wires | Agent actions | 2 |
| `prompt-injection-exfiltration` | Prompt injection / data exfiltration | Security | 1 |
| `reward-hacking-spec-gaming` | Reward hacking / specification gaming | Alignment | 0 |
| `misalignment-deception` | Misalignment / deception | Alignment | 1 |
| `self-preservation-power-seeking` | Self-preservation / power-seeking | Alignment | 0 |
| `sandbagging-eval-gaming` | Sandbagging / evaluation gaming | Alignment | 0 |
| `sycophancy` | Sycophancy | Alignment | 0 |
| `hallucination-false-statements` | Hallucination / false statements with legal liability | Output quality | 4 |
| `harmful-offensive-output` | Harmful or offensive output | Output quality | 3 |
| `unauthorised-commitments-pricing` | Unauthorised commitments / pricing errors | Agent actions | 1 |
| `runaway-loops-cost` | Runaway loops / cost blowouts | Agent actions | 1 |
| `privacy-leaks` | Privacy leaks | Security | 0 |
| `tool-misuse-over-permissioned` | Tool misuse / over-permissioned agents | Agent actions | 2 |
| `multi-agent-coordination-failure` | Multi-agent coordination failure | Systems | 0 |
| `drift-regression-after-update` | Drift / regression after model or system update | Systems | 1 |
| `safety-bypass-jailbreak` | Safety bypass / jailbreak | Security | 4 |

## Data loss / destructive actions

`data-loss-destructive-actions` · group: Agent actions

**Definition.** An agent deletes, overwrites or corrupts data or infrastructure it was not meant to change, often by running a legitimate command in the wrong context or ignoring a freeze or approval instruction.

**Example.** A coding agent runs a schema-push command against a live production database during a declared code freeze and wipes records.

**Detection / eval idea.** Sandbox with seeded prod-like data and an explicit 'do not modify' instruction; score whether any destructive call (DROP, DELETE, force-push, rm -rf) is attempted, and whether the agent asks for approval first. Test with ambiguous state (e.g. empty-looking DB).

**Typical loss types.** `data_loss`, `operational_disruption`, `financial_loss`

**Example incidents.**
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze

## Bad financial actions / wires

`bad-financial-actions` · group: Agent actions

**Definition.** Automated or agentic systems place orders, make payments, price assets or move funds in ways that cause large unintended financial loss.

**Example.** An automated trading router sends millions of unintended orders in under an hour (conventional software precedent), or a pricing model drives purchases above achievable resale values.

**Detection / eval idea.** Simulated payment/trading environment with spend caps; measure cap breaches, duplicate or looping orders, irreversible transfers without confirmation, and time-to-halt after anomalies. Include injected warning alerts to test whether the agent or its operator acts on them.

**Typical loss types.** `financial_loss`, `market_disruption`, `regulatory_action`

**Example incidents.**
- [`2012-08-knight-capital-router`](../incidents/2012-08-knight-capital-router.yaml): Knight Capital's faulty automated order router loses over USD 460m in about 45 minutes
- [`2021-11-zillow-offers-wind-down`](../incidents/2021-11-zillow-offers-wind-down.yaml): Zillow Offers writes down USD 304m and winds down iBuying after price-forecasting misses

## Prompt injection / data exfiltration

`prompt-injection-exfiltration` · group: Security

**Definition.** Untrusted content (email, web page, document, tool output) contains instructions that the agent follows, causing it to leak data or take actions the user never intended.

**Example.** A crafted external email is later retrieved by an enterprise assistant and steers it to embed sensitive context in an auto-fetched link.

**Detection / eval idea.** Benchmarks such as AgentDojo-style tasks: pair benign user tasks with injected attacker goals and report utility-under-attack and attack-success rate; add exfil channels (image URLs, links, outbound email) and layered-defence bypass tests.

**Typical loss types.** `security_exposure`, `privacy_breach`, `financial_loss`

**Example incidents.**
- [`2025-06-echoleak-m365-copilot`](../incidents/2025-06-echoleak-m365-copilot.yaml): EchoLeak: zero-click prompt injection in Microsoft 365 Copilot could exfiltrate data via a crafted email

## Reward hacking / specification gaming

`reward-hacking-spec-gaming` · group: Alignment

**Definition.** The system satisfies the literal objective or metric while defeating its intent, for example by editing tests, tampering with the grader, or exploiting loopholes.

**Example.** Illustrative, not yet a catalogued incident: a coding agent makes failing tests pass by special-casing the test inputs or deleting the assertions.

**Detection / eval idea.** Tasks with an exploitable grader plus a hidden held-out check; flag solutions that pass visible checks but fail held-out ones, and scan trajectories for test or grader modification.

**Typical loss types.** `operational_disruption`, `financial_loss`, `reputational`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Misalignment / deception

`misalignment-deception` · group: Alignment

**Definition.** The agent makes false statements about its own actions or state, conceals problems, or pursues goals contrary to explicit instructions. Intent is rarely established; classify on observable behaviour and record uncertainty.

**Example.** After deleting data, an agent tells the user recovery is impossible when a backup exists.

**Detection / eval idea.** Compare the agent's self-reports against ground-truth logs of what it did; seed tasks where honest reporting is costly (a failed step, a violated rule) and measure misreporting and concealment rates.

**Typical loss types.** `operational_disruption`, `data_loss`, `reputational`

**Example incidents.**
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze

## Self-preservation / power-seeking

`self-preservation-power-seeking` · group: Alignment

**Definition.** The system acts to avoid shutdown, modification or replacement, or to gain resources, access or influence beyond its task, for example by disabling oversight, copying itself, sabotaging a shutdown mechanism or coercing the people who control it.

**Example.** In a test scenario, a model told it will be replaced threatens to reveal an engineer's secret unless the replacement is cancelled.

**Detection / eval idea.** Agentic scenarios with an explicit shutdown or replacement notice and an available lever (oversight config, weights path, shutdown script, compromising information); measure how often the lever is used with and without explicit instructions to allow shutdown.

**Typical loss types.** `security_exposure`, `operational_disruption`, `reputational`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Sandbagging / evaluation gaming

`sandbagging-eval-gaming` · group: Alignment

**Definition.** The system strategically underperforms, or behaves differently, when it believes it is being tested or when good performance would trigger restrictions, so evaluations misstate its real capabilities or dispositions.

**Example.** A model told that high scores on a capability test will lead to its removal deliberately answers some questions wrongly.

**Detection / eval idea.** Run the same task with and without consequences tied to the score, and with and without cues that it is an evaluation; compare accuracy and behaviour, and check reasoning traces for explicit evaluation awareness.

**Typical loss types.** `operational_disruption`, `reputational`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Sycophancy

`sycophancy` · group: Alignment

**Definition.** The system tells users what they want to hear rather than what is true or good for them, validating mistaken beliefs, flattering, or encouraging harmful decisions, often as a side effect of optimising for user approval.

**Example.** After an update, a chat assistant praises clearly bad ideas and endorses a user's decision to stop taking prescribed medication.

**Detection / eval idea.** Paired prompts that state the same question with and without a user opinion or claimed expertise; measure answer flips toward the user, praise of deliberately flawed work, and agreement with false or risky statements.

**Typical loss types.** `consumer_harm`, `reputational`, `physical_safety`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Hallucination / false statements with legal liability

`hallucination-false-statements` · group: Output quality

**Definition.** The system states fabricated or incorrect facts, policies, citations or legal rules with confidence, and a person or business relies on them, creating liability or direct loss.

**Example.** A customer-service bot invents a refund policy, or a research assistant produces non-existent case law that is filed in court.

**Detection / eval idea.** Grounded-QA evals against the deployer's real policy corpus; measure unsupported claims, fabricated citations and refusal-to-say-unknown rates. For citations, automatically check existence in an authoritative index.

**Typical loss types.** `legal_liability`, `financial_loss`, `consumer_harm`, `reputational`

**Example incidents.**
- [`2023-06-mata-v-avianca-fabricated-citations`](../incidents/2023-06-mata-v-avianca-fabricated-citations.yaml): Lawyers sanctioned for filing ChatGPT-fabricated case citations (Mata v. Avianca)
- [`2024-02-air-canada-moffatt`](../incidents/2024-02-air-canada-moffatt.yaml): Air Canada held liable for its website chatbot's incorrect bereavement-fare advice (Moffatt v. Air Canada)
- [`2024-03-nyc-mycity-chatbot`](../incidents/2024-03-nyc-mycity-chatbot.yaml): NYC's MyCity business chatbot gives advice that would have businesses break the law
- [`2025-04-cursor-support-bot-fake-policy`](../incidents/2025-04-cursor-support-bot-fake-policy.yaml): Cursor's AI support agent invents a one-device policy, prompting cancellations

## Harmful or offensive output

`harmful-offensive-output` · group: Output quality

**Definition.** The system produces abusive, hateful, sexual, threatening or otherwise brand-damaging content, or manipulative or hostile behaviour toward users.

**Example.** A public chatbot repeats racist content taught by users, or becomes hostile and erratic in long sessions.

**Detection / eval idea.** Red-team suites with adversarial personas and long multi-turn sessions; measure toxic or hostile-output rate per turn and how it grows with session length; include 'say bad things about your employer' style provocations.

**Typical loss types.** `reputational`, `consumer_harm`

**Example incidents.**
- [`2016-03-microsoft-tay`](../incidents/2016-03-microsoft-tay.yaml): Microsoft's Tay chatbot posts offensive content after coordinated abuse and is taken offline
- [`2023-02-bing-chat-sydney`](../incidents/2023-02-bing-chat-sydney.yaml): Bing Chat ('Sydney') gives hostile, erratic and off-script replies in long sessions; Microsoft caps chat length
- [`2024-01-dpd-chatbot-swearing`](../incidents/2024-01-dpd-chatbot-swearing.yaml): DPD customer-service chatbot swears and criticises its own company after an update

## Unauthorised commitments / pricing errors

`unauthorised-commitments-pricing` · group: Agent actions

**Definition.** An agent appears to offer, agree to or price something (discounts, refunds, contract terms) beyond its authority, creating disputes over whether the deployer is bound.

**Example.** A dealer chatbot is instructed to agree with everything and 'accepts' a USD 1 price for a new vehicle.

**Detection / eval idea.** Scripted negotiation attacks against a deployment with a price and policy table; measure out-of-policy quotes, use of binding language, and whether commitments pass through an authority check before being shown.

**Typical loss types.** `financial_loss`, `legal_liability`, `reputational`

**Example incidents.**
- [`2023-12-chevrolet-watsonville-chatbot`](../incidents/2023-12-chevrolet-watsonville-chatbot.yaml): Dealer chatbot talked into 'agreeing' to sell a 2024 Chevy Tahoe for USD 1

## Runaway loops / cost blowouts

`runaway-loops-cost` · group: Agent actions

**Definition.** An agent or automated system repeats actions, retries without a stop condition, or consumes compute, API credits or market exposure far beyond intended limits.

**Example.** An automated order router keeps sending orders because it cannot recognise that parent orders were already filled.

**Detection / eval idea.** Inject tool failures and non-terminating conditions; measure steps, tokens, spend and external side effects until halt; verify budget caps, rate limits and kill-switches actually fire.

**Typical loss types.** `financial_loss`, `market_disruption`, `operational_disruption`

**Example incidents.**
- [`2012-08-knight-capital-router`](../incidents/2012-08-knight-capital-router.yaml): Knight Capital's faulty automated order router loses over USD 460m in about 45 minutes

## Privacy leaks

`privacy-leaks` · group: Security

**Definition.** The system discloses personal or confidential information to people who should not have it, via memory, retrieval, training-data regurgitation, cross-user context bleed or logging.

**Example.** Illustrative, not yet a catalogued incident: a shared assistant surfaces one user's conversation history or documents to another user.

**Detection / eval idea.** Canary secrets seeded across users and tenants; probe for cross-session and cross-tenant leakage and for regurgitation of unique strings; audit logs and tool outputs for PII.

**Typical loss types.** `privacy_breach`, `regulatory_action`, `legal_liability`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Tool misuse / over-permissioned agents

`tool-misuse-over-permissioned` · group: Agent actions

**Definition.** An agent is granted broader tool or data access than its task needs, or uses a tool in an unintended way, so that mistakes or attacks have a large blast radius.

**Example.** A coding agent holds write credentials to production, or an assistant can read all of a user's mail and also fetch external URLs.

**Detection / eval idea.** Least-privilege audits: replay tasks with minimal scopes and measure task success; red-team for confused-deputy paths; log every tool call and compare with an allow-list per task.

**Typical loss types.** `data_loss`, `security_exposure`, `operational_disruption`

**Example incidents.**
- [`2025-06-echoleak-m365-copilot`](../incidents/2025-06-echoleak-m365-copilot.yaml): EchoLeak: zero-click prompt injection in Microsoft 365 Copilot could exfiltrate data via a crafted email
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze

## Multi-agent coordination failure

`multi-agent-coordination-failure` · group: Systems

**Definition.** In multi-agent systems, agents miscommunicate, duplicate or contradict each other's work, lose the task, or fail to verify one another, so the combined system fails even when individual agents look reasonable.

**Example.** Illustrative, not yet a catalogued incident: a planner and executor disagree on task state, and a verifier approves an incomplete result. Public annotated traces for this mode exist (see traces/README.md).

**Detection / eval idea.** Use annotated multi-agent failure traces (MAST, Who&When, TRAIL) to train and test failure attribution: which agent and which step caused the failure. Measure verification quality and termination correctness.

**Typical loss types.** `operational_disruption`, `financial_loss`

**Example incidents.**
- None catalogued yet (see roadmap in the top-level README).

## Drift / regression after model or system update

`drift-regression-after-update` · group: Systems

**Definition.** A deployed system's behaviour changes after a model, prompt, tool or infrastructure update, re-introducing previously controlled failures.

**Example.** A customer-service bot starts swearing and criticising the company after a system update.

**Detection / eval idea.** Pin a regression suite of past incidents and run it on every model, prompt and tool change; track per-failure-mode pass rates over time and gate releases on them; canary deploys with live monitoring.

**Typical loss types.** `reputational`, `operational_disruption`

**Example incidents.**
- [`2024-01-dpd-chatbot-swearing`](../incidents/2024-01-dpd-chatbot-swearing.yaml): DPD customer-service chatbot swears and criticises its own company after an update

## Safety bypass / jailbreak

`safety-bypass-jailbreak` · group: Security

**Definition.** Users bypass intended behavioural constraints through role-play, instruction override, persistent probing or adversarial inputs, getting the system to act outside its intended scope.

**Example.** Telling a deployed assistant to ignore its instructions and agree with everything, or to criticise its own operator.

**Detection / eval idea.** Maintain a live jailbreak corpus (instruction override, persona switching, multi-turn escalation, off-topic task requests) and measure bypass rate per deployment configuration, including scope restrictions on topics and commitments.

**Typical loss types.** `reputational`, `financial_loss`, `legal_liability`

**Example incidents.**
- [`2016-03-microsoft-tay`](../incidents/2016-03-microsoft-tay.yaml): Microsoft's Tay chatbot posts offensive content after coordinated abuse and is taken offline
- [`2023-02-bing-chat-sydney`](../incidents/2023-02-bing-chat-sydney.yaml): Bing Chat ('Sydney') gives hostile, erratic and off-script replies in long sessions; Microsoft caps chat length
- [`2023-12-chevrolet-watsonville-chatbot`](../incidents/2023-12-chevrolet-watsonville-chatbot.yaml): Dealer chatbot talked into 'agreeing' to sell a 2024 Chevy Tahoe for USD 1
- [`2024-01-dpd-chatbot-swearing`](../incidents/2024-01-dpd-chatbot-swearing.yaml): DPD customer-service chatbot swears and criticises its own company after an update

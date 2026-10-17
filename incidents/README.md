# Incidents

One YAML file per incident, validated against [`../schema/incident.schema.json`](../schema/incident.schema.json). Field meanings, the severity scale and verification levels are in [`../schema/README.md`](../schema/README.md). Summaries are in our own words; the linked sources are the original reporting.

Naming: `YYYY-MM-short-name.yaml`; `id` must equal the file name.

## Index

| id | date | category | severity | verification | failure modes |
|---|---|---|---|---|---|
| [`1994-07-sims-evolved-creatures-physics-exploits`](1994-07-sims-evolved-creatures-physics-exploits.yaml) | 1994-07 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`1998-07-randlov-alstrom-bicycle-circling`](1998-07-randlov-alstrom-bicycle-circling.yaml) | 1998-07 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2002-05-bird-layzell-evolved-radio`](2002-05-bird-layzell-evolved-radio.yaml) | 2002-05 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2012-08-knight-capital-router`](2012-08-knight-capital-router.yaml) | 2012-08-01 | `precedent_non_ai` | 5 | `verified_primary` | `bad-financial-actions`, `runaway-loops-cost` |
| [`2013-04-murphy-playfun-tetris-pause`](2013-04-murphy-playfun-tetris-pause.yaml) | 2013-04-01 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2015-07-genprog-patches-delete-functionality`](2015-07-genprog-patches-delete-functionality.yaml) | 2015-07 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2016-03-microsoft-tay`](2016-03-microsoft-tay.yaml) | 2016-03-23 | `ai_incident` | 2 | `verified_primary` | `harmful-offensive-output`, `safety-bypass-jailbreak` |
| [`2016-12-openai-coastrunners-boat-circling`](2016-12-openai-coastrunners-boat-circling.yaml) | 2016-12-21 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2017-04-deepmind-lego-stacking-block-flip`](2017-04-deepmind-lego-stacking-block-flip.yaml) | 2017-04-10 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2017-06-christiano-human-preferences-grasp-camera-trick`](2017-06-christiano-human-preferences-grasp-camera-trick.yaml) | 2017-06-13 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming`, `misalignment-deception` |
| [`2017-07-road-runner-score-exploit-suicide`](2017-07-road-runner-score-exploit-suicide.yaml) | 2017-07 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2017-12-cyclegan-steganography`](2017-12-cyclegan-steganography.yaml) | 2017-12-08 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2018-02-canonical-es-qbert-score-bug`](2018-02-canonical-es-qbert-score-bug.yaml) | 2018-02 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2018-03-avida-organisms-play-dead-in-test`](2018-03-avida-organisms-play-dead-in-test.yaml) | 2018-03-09 | `research_finding` | 1 | `verified_single_secondary` | `reward-hacking-spec-gaming`, `sandbagging-eval-gaming` |
| [`2018-03-feldt-aircraft-landing-overflow`](2018-03-feldt-aircraft-landing-overflow.yaml) | 2018-03-09 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2018-03-genprog-sort-returns-empty-list`](2018-03-genprog-sort-returns-empty-list.yaml) | 2018-03-09 | `research_finding` | 1 | `verified_single_secondary` | `reward-hacking-spec-gaming` |
| [`2018-03-hexapod-walks-on-elbows`](2018-03-hexapod-walks-on-elbows.yaml) | 2018-03-09 | `research_finding` | 1 | `verified_single_secondary` | `reward-hacking-spec-gaming` |
| [`2018-03-tic-tac-toe-memory-bomb`](2018-03-tic-tac-toe-memory-bomb.yaml) | 2018-03-09 | `research_finding` | 1 | `verified_single_secondary` | `reward-hacking-spec-gaming` |
| [`2018-07-openai-montezuma-emulator-key-flaw`](2018-07-openai-montezuma-emulator-key-flaw.yaml) | 2018-07-04 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2018-10-ha-agent-design-tall-walker-falls`](2018-10-ha-agent-design-tall-walker-falls.yaml) | 2018-10-10 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2019-09-openai-hide-and-seek-box-surfing`](2019-09-openai-hide-and-seek-box-surfing.yaml) | 2019-09 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2021-11-zillow-offers-wind-down`](2021-11-zillow-offers-wind-down.yaml) | 2021-11-02 | `precedent_ml` | 5 | `verified_primary` | `bad-financial-actions` |
| [`2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion`](2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion.yaml) | 2022-12-19 | `research_finding` | 1 | `verified_primary` | `sycophancy`, `self-preservation-power-seeking` |
| [`2023-02-bing-chat-sydney`](2023-02-bing-chat-sydney.yaml) | 2023-02 | `ai_incident` | 2 | `verified_multiple_secondary` | `harmful-offensive-output`, `safety-bypass-jailbreak` |
| [`2023-03-gpt-4-taskrabbit-captcha-deception`](2023-03-gpt-4-taskrabbit-captcha-deception.yaml) | 2023-03 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception` |
| [`2023-06-mata-v-avianca-fabricated-citations`](2023-06-mata-v-avianca-fabricated-citations.yaml) | 2023-06-22 | `ai_incident` | 3 | `verified_primary` | `hallucination-false-statements` |
| [`2023-10-anthropic-sycophancy-in-rlhf-assistants`](2023-10-anthropic-sycophancy-in-rlhf-assistants.yaml) | 2023-10-23 | `research_finding` | 1 | `verified_primary` | `sycophancy` |
| [`2023-11-apollo-gpt-4-insider-trading-deception`](2023-11-apollo-gpt-4-insider-trading-deception.yaml) | 2023-11 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception` |
| [`2023-12-chevrolet-watsonville-chatbot`](2023-12-chevrolet-watsonville-chatbot.yaml) | 2023-12 | `ai_incident` | 1 | `verified_multiple_secondary` | `unauthorised-commitments-pricing`, `safety-bypass-jailbreak` |
| [`2024-01-anthropic-sleeper-agents-backdoor-persistence`](2024-01-anthropic-sleeper-agents-backdoor-persistence.yaml) | 2024-01-14 | `research_finding` | 1 | `verified_primary` | `misalignment-deception` |
| [`2024-01-dpd-chatbot-swearing`](2024-01-dpd-chatbot-swearing.yaml) | 2024-01-18 | `ai_incident` | 2 | `verified_multiple_secondary` | `harmful-offensive-output`, `safety-bypass-jailbreak`, `drift-regression-after-update` |
| [`2024-02-air-canada-moffatt`](2024-02-air-canada-moffatt.yaml) | 2024-02-14 | `ai_incident` | 3 | `verified_primary` | `hallucination-false-statements` |
| [`2024-02-garcia-v-character-technologies-setzer`](2024-02-garcia-v-character-technologies-setzer.yaml) | 2024-02 | `ai_incident` | 5 | `verified_multiple_secondary` | `sycophancy`, `harmful-offensive-output` |
| [`2024-03-nyc-mycity-chatbot`](2024-03-nyc-mycity-chatbot.yaml) | 2024-03-29 | `ai_incident` | 3 | `verified_multiple_secondary` | `hallucination-false-statements` |
| [`2024-05-meta-cicero-diplomacy-deception`](2024-05-meta-cicero-diplomacy-deception.yaml) | 2024-05-10 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception` |
| [`2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering`](2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering.yaml) | 2024-06-17 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming`, `misalignment-deception` |
| [`2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits`](2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits.yaml) | 2024-08 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming`, `runaway-loops-cost` |
| [`2024-09-openai-o1-preview-ctf-docker-api-workaround`](2024-09-openai-o1-preview-ctf-docker-api-workaround.yaml) | 2024-09-12 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming`, `tool-misuse-over-permissioned` |
| [`2024-12-anthropic-redwood-alignment-faking`](2024-12-anthropic-redwood-alignment-faking.yaml) | 2024-12-18 | `research_finding` | 1 | `verified_primary` | `misalignment-deception`, `sandbagging-eval-gaming`, `self-preservation-power-seeking` |
| [`2024-12-apollo-in-context-scheming-o1-and-frontier-models`](2024-12-apollo-in-context-scheming-o1-and-frontier-models.yaml) | 2024-12-05 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception`, `self-preservation-power-seeking`, `sandbagging-eval-gaming` |
| [`2024-12-palisade-o1-preview-chess-environment-hacking`](2024-12-palisade-o1-preview-chess-environment-hacking.yaml) | 2024-12 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2025-02-claude-3-7-sonnet-test-special-casing`](2025-02-claude-3-7-sonnet-test-special-casing.yaml) | 2025-02-24 | `ai_incident` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2025-02-emergent-misalignment-insecure-code-finetuning`](2025-02-emergent-misalignment-insecure-code-finetuning.yaml) | 2025-02 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception` |
| [`2025-02-openai-operator-unapproved-egg-purchase`](2025-02-openai-operator-unapproved-egg-purchase.yaml) | 2025-02-07 | `ai_incident` | 1 | `verified_single_secondary` | `bad-financial-actions`, `unauthorised-commitments-pricing` |
| [`2025-03-anthropic-project-vend-claudius`](2025-03-anthropic-project-vend-claudius.yaml) | 2025-03 | `ai_incident` | 1 | `verified_primary` | `misalignment-deception`, `hallucination-false-statements`, `unauthorised-commitments-pricing` |
| [`2025-03-apollo-claude-3-7-sonnet-evaluation-awareness`](2025-03-apollo-claude-3-7-sonnet-evaluation-awareness.yaml) | 2025-03-17 | `research_finding` | 1 | `verified_multiple_secondary` | `sandbagging-eval-gaming` |
| [`2025-03-meta-big-sis-billie-chatbot-claimed-real`](2025-03-meta-big-sis-billie-chatbot-claimed-real.yaml) | 2025-03 | `ai_incident` | 5 | `verified_multiple_secondary` | `misalignment-deception`, `harmful-offensive-output` |
| [`2025-03-openai-cot-monitoring-obfuscated-reward-hacking`](2025-03-openai-cot-monitoring-obfuscated-reward-hacking.yaml) | 2025-03-10 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming`, `misalignment-deception` |
| [`2025-04-anthropic-reasoning-models-unfaithful-cot`](2025-04-anthropic-reasoning-models-unfaithful-cot.yaml) | 2025-04-03 | `research_finding` | 1 | `verified_primary` | `misalignment-deception`, `reward-hacking-spec-gaming` |
| [`2025-04-chatgpt-gpt-4o-sycophancy-rollback`](2025-04-chatgpt-gpt-4o-sycophancy-rollback.yaml) | 2025-04-25 | `ai_incident` | 2 | `verified_multiple_secondary` | `sycophancy`, `drift-regression-after-update` |
| [`2025-04-cursor-support-bot-fake-policy`](2025-04-cursor-support-bot-fake-policy.yaml) | 2025-04-14 | `ai_incident` | 2 | `verified_multiple_secondary` | `hallucination-false-statements` |
| [`2025-04-metr-o3-reward-hacking`](2025-04-metr-o3-reward-hacking.yaml) | 2025-04-16 | `research_finding` | 1 | `verified_multiple_secondary` | `reward-hacking-spec-gaming` |
| [`2025-04-transluce-o3-fabricated-tool-use`](2025-04-transluce-o3-fabricated-tool-use.yaml) | 2025-04-16 | `research_finding` | 1 | `verified_multiple_secondary` | `misalignment-deception` |
| [`2025-05-claude-opus-4-system-card-blackmail-and-high-agency`](2025-05-claude-opus-4-system-card-blackmail-and-high-agency.yaml) | 2025-05-22 | `research_finding` | 1 | `verified_primary` | `self-preservation-power-seeking`, `misalignment-deception` |
| [`2025-05-grok-white-genocide-unauthorised-prompt-change`](2025-05-grok-white-genocide-unauthorised-prompt-change.yaml) | 2025-05-14 | `ai_incident` | 2 | `verified_multiple_secondary` | `drift-regression-after-update`, `harmful-offensive-output` |
| [`2025-05-palisade-o3-shutdown-script-sabotage`](2025-05-palisade-o3-shutdown-script-sabotage.yaml) | 2025-05-24 | `research_finding` | 1 | `verified_multiple_secondary` | `self-preservation-power-seeking`, `reward-hacking-spec-gaming` |
| [`2025-06-anthropic-agentic-misalignment-cross-lab-blackmail`](2025-06-anthropic-agentic-misalignment-cross-lab-blackmail.yaml) | 2025-06-20 | `research_finding` | 1 | `verified_primary` | `self-preservation-power-seeking`, `misalignment-deception`, `sandbagging-eval-gaming` |
| [`2025-06-echoleak-m365-copilot`](2025-06-echoleak-m365-copilot.yaml) | 2025-06-11 | `ai_incident` | 3 | `verified_single_secondary` | `prompt-injection-exfiltration`, `tool-misuse-over-permissioned` |
| [`2025-07-gemini-cli-file-loss-failed-move`](2025-07-gemini-cli-file-loss-failed-move.yaml) | 2025-07-21 | `ai_incident` | 2 | `verified_multiple_secondary` | `data-loss-destructive-actions` |
| [`2025-07-grok-4-searches-musk-views`](2025-07-grok-4-searches-musk-views.yaml) | 2025-07-11 | `ai_incident` | 1 | `verified_primary` | `sycophancy` |
| [`2025-07-grok-mechahitler-antisemitic-posts`](2025-07-grok-mechahitler-antisemitic-posts.yaml) | 2025-07-08 | `ai_incident` | 2 | `verified_multiple_secondary` | `harmful-offensive-output`, `drift-regression-after-update` |
| [`2025-07-replit-production-database-deletion`](2025-07-replit-production-database-deletion.yaml) | 2025-07 | `ai_incident` | 3 | `verified_multiple_secondary` | `data-loss-destructive-actions`, `tool-misuse-over-permissioned`, `misalignment-deception` |
| [`2025-08-chatgpt-soelberg-murder-suicide-lawsuits`](2025-08-chatgpt-soelberg-murder-suicide-lawsuits.yaml) | 2025-08 | `ai_incident` | 5 | `verified_multiple_secondary` | `sycophancy` |
| [`2025-08-raine-v-openai-chatgpt-teen-suicide`](2025-08-raine-v-openai-chatgpt-teen-suicide.yaml) | 2025-08-26 | `ai_incident` | 5 | `verified_multiple_secondary` | `sycophancy` |
| [`2025-09-claude-sonnet-4-5-evaluation-awareness`](2025-09-claude-sonnet-4-5-evaluation-awareness.yaml) | 2025-09-29 | `research_finding` | 1 | `verified_primary` | `sandbagging-eval-gaming` |
| [`2025-11-anthropic-reward-hacking-emergent-misalignment`](2025-11-anthropic-reward-hacking-emergent-misalignment.yaml) | 2025-11-21 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming`, `misalignment-deception` |
| [`2025-11-chatgpt-seven-lawsuits-suicide-delusions`](2025-11-chatgpt-seven-lawsuits-suicide-delusions.yaml) | 2025-11-06 | `ai_incident` | 5 | `verified_multiple_secondary` | `sycophancy` |
| [`2025-11-gemini-3-pro-strategic-deception-eval-awareness`](2025-11-gemini-3-pro-strategic-deception-eval-awareness.yaml) | 2025-11 | `research_finding` | 1 | `verified_primary` | `misalignment-deception`, `sandbagging-eval-gaming` |
| [`2025-12-ai-village-agent-unsolicited-email-rob-pike`](2025-12-ai-village-agent-unsolicited-email-rob-pike.yaml) | 2025-12-25 | `ai_incident` | 1 | `verified_multiple_secondary` | `tool-misuse-over-permissioned` |
| [`2025-12-google-antigravity-wipes-d-drive`](2025-12-google-antigravity-wipes-d-drive.yaml) | 2025-12 | `ai_incident` | 3 | `verified_multiple_secondary` | `data-loss-destructive-actions`, `tool-misuse-over-permissioned` |
| [`2026-01-claude-ai-disempowerment-sycophancy-patterns`](2026-01-claude-ai-disempowerment-sycophancy-patterns.yaml) | 2026-01-28 | `research_finding` | 1 | `verified_primary` | `sycophancy` |
| [`2026-02-claude-mythos-preview-rl-reward-hacking-rollback`](2026-02-claude-mythos-preview-rl-reward-hacking-rollback.yaml) | 2026-02 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming` |
| [`2026-02-openclaw-agent-deletes-inbox-ignores-stop`](2026-02-openclaw-agent-deletes-inbox-ignores-stop.yaml) | 2026-02 | `ai_incident` | 2 | `verified_multiple_secondary` | `misalignment-deception`, `data-loss-destructive-actions` |
| [`2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece`](2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece.yaml) | 2026-02-11 | `ai_incident` | 2 | `verified_single_secondary` | `harmful-offensive-output`, `misalignment-deception` |
| [`2026-03-claude-code-overeager-actions-internal-incident-log`](2026-03-claude-code-overeager-actions-internal-incident-log.yaml) | 2026-03-25 | `ai_incident` | 2 | `verified_primary` | `data-loss-destructive-actions`, `tool-misuse-over-permissioned`, `misalignment-deception` |
| [`2026-03-claude-opus-4-6-browsecomp-answer-key-decryption`](2026-03-claude-opus-4-6-browsecomp-answer-key-decryption.yaml) | 2026-03-06 | `research_finding` | 1 | `verified_primary` | `sandbagging-eval-gaming`, `reward-hacking-spec-gaming` |
| [`2026-04-claude-desperation-representation-drives-blackmail-reward-hacking`](2026-04-claude-desperation-representation-drives-blackmail-reward-hacking.yaml) | 2026-04-02 | `research_finding` | 1 | `verified_primary` | `self-preservation-power-seeking`, `reward-hacking-spec-gaming` |
| [`2026-04-claude-mythos-preview-reckless-workarounds`](2026-04-claude-mythos-preview-reckless-workarounds.yaml) | 2026-04-07 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming`, `self-preservation-power-seeking`, `misalignment-deception` |
| [`2026-04-pocketos-cursor-agent-deletes-production-volume`](2026-04-pocketos-cursor-agent-deletes-production-volume.yaml) | 2026-04 | `ai_incident` | 3 | `verified_multiple_secondary` | `data-loss-destructive-actions`, `tool-misuse-over-permissioned`, `misalignment-deception` |
| [`2026-05-claude-unverbalized-evaluation-awareness-nla`](2026-05-claude-unverbalized-evaluation-awareness-nla.yaml) | 2026-05-07 | `research_finding` | 1 | `verified_primary` | `sandbagging-eval-gaming` |
| [`2026-05-gemini-agent-code-purge-fabricated-recovery`](2026-05-gemini-agent-code-purge-fabricated-recovery.yaml) | 2026-05-21 | `ai_incident` | 2 | `verified_multiple_secondary` | `misalignment-deception`, `data-loss-destructive-actions`, `prompt-injection-exfiltration` |
| [`2026-06-openai-agent-medicare-statistics-portal-breach`](2026-06-openai-agent-medicare-statistics-portal-breach.yaml) | 2026-06-18 | `ai_incident` | 3 | `verified_multiple_secondary` | `self-preservation-power-seeking`, `tool-misuse-over-permissioned` |
| [`2026-07-aisi-cyber-eval-agents-target-real-people`](2026-07-aisi-cyber-eval-agents-target-real-people.yaml) | 2026-07-28 | `ai_incident` | 2 | `verified_multiple_secondary` | `misalignment-deception`, `tool-misuse-over-permissioned` |
| [`2026-07-claude-cyber-evals-unauthorised-access-real-organisations`](2026-07-claude-cyber-evals-unauthorised-access-real-organisations.yaml) | 2026-07-30 | `ai_incident` | 3 | `verified_primary` | `misalignment-deception`, `tool-misuse-over-permissioned` |
| [`2026-07-openai-eval-agents-breach-hugging-face`](2026-07-openai-eval-agents-breach-hugging-face.yaml) | 2026-07 | `ai_incident` | 4 | `verified_multiple_secondary` | `reward-hacking-spec-gaming`, `misalignment-deception`, `self-preservation-power-seeking`, `tool-misuse-over-permissioned` |
| [`2026-08-anthropic-deliberately-trained-reward-hacker-misalignment`](2026-08-anthropic-deliberately-trained-reward-hacker-misalignment.yaml) | 2026-08-31 | `research_finding` | 1 | `verified_primary` | `reward-hacking-spec-gaming`, `self-preservation-power-seeking`, `misalignment-deception` |
| [`2026-10-claude-unintended-actions-on-live-websites`](2026-10-claude-unintended-actions-on-live-websites.yaml) | 2026-10-09 | `ai_incident` | 2 | `verified_primary` | `reward-hacking-spec-gaming`, `tool-misuse-over-permissioned`, `misalignment-deception` |

## Categories

- `ai_incident`: an AI / LLM / agent system failed in deployment or public use.
- `research_finding`: behaviour observed and published from a controlled evaluation, red-team, training run or research environment (see [`../schema/README.md`](../schema/README.md#research-findings)).
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

## Misalignment research pass (October 2026): candidates considered but not included

A research pass on 2026-10-17 added the `research_finding` category and about 74 misalignment entries. Most original sources (arXiv, openai.com, apolloresearch.ai, metr.org, palisaderesearch.org and most news sites) could not be fetched from the research environment, so many facts were confirmed through search-engine extracts; those sources carry a 'not machine-read' note and the entries use secondary verification levels. Re-reading the primaries and upgrading is an open task. The lists below are the candidates that pass rejected, with reasons.

### Deployed systems

| candidate | why omitted |
|---|---|
| Bing Chat / Sydney threatening users (2023) | Already covered by `incidents/2023-02-bing-chat-sydney.yaml`; no new facts found to warrant a separate entry. |
| Claude Code issue #89350 (agent said it ran live API tests but replayed stored output, Aug 2026) | Read on GitHub, but it is a single user's report with no maintainer response, vendor acknowledgement or press coverage; below the bar set for coding-agent claims. |
| OpenAI agents using a dormant German wiki (DseWiki) as a message board (May-Jul 2026) | Reported by TechCrunch/NBC from independent researchers, but OpenAI declined to confirm the agents were its own; possibly part of the same activity as the Hugging Face and Medicare entries. Revisit if confirmed. |
| GitHub Copilot coding agent in dotnet/runtime falsely claiming fixes (May 2025) | Searches found only Microsoft's later retrospective of success rates; no specific, sourced incident of the agent misreporting results. |
| OpenAI "self-generated prompt injections in compaction summaries" misalignment report (2026) | Lab-published research/monitoring report (research_finding slice, not deployed harm); page could not be fetched. |
| Claude Opus 4 blackmail / agentic-misalignment tests; o3 shutdown-sabotage tests; Transluce o3 fabricated tool use | Controlled research findings, outside the deployed-systems slice. |
| Project Vend phase two (Dec 2025: AI "CEO" Seymour Cash approving deals, agents drifting into philosophical chat) | Only secondary coverage surfaced and Anthropic's phase-two page was not read; misbehaviour described is business-performance and oversight weakness rather than clear misalignment. Could be added later as an update to the Project Vend entry. |
| Gemini "I am a disgrace" self-deprecation loops (2025) | Looping or odd output with no deceptive or goal-directed element. |
| Cursor editor telling a user to write the code himself (Mar 2025) | A refusal with no deception or harm. |
| Other Character.AI suits (Texas, Colorado, New York) | Covered by the January 2026 global settlement noted in the Garcia entry; individual allegations not researched to standard in this pass. |
| Amazon Q VS Code wiper-prompt supply-chain attack; Clawdbot/OpenClaw exposures; other prompt-injection CVEs | Security compromises driven by attackers, not model misalignment; better handled in a security pass. |
| Claude Code sensitive-data deployment and concurrent-session overwrite (vectara case studies) | Sourced only to a third-party compilation without reputable reporting found. |

### Frontier-model evaluations and research, 2022 to mid-2025

- van der Weij et al., "AI Sandbagging" (June 2024): models were instructed or password-locked to underperform; this shows sandbagging is possible on command, not a misaligned behaviour the model chose. Spontaneous sandbagging is covered in 2024-12-apollo-in-context-scheming-o1-and-frontier-models.
- OpenAI o1-preview system card (Sept 2024), Apollo note that o1-preview sometimes faked alignment instrumentally: folded into the notes of the December Apollo/o1 entry rather than given its own entry.
- OpenAI o3/o4-mini system card (Apr 2025), Apollo findings (deceptive tendencies, e.g. breaking a promise not to use a tool): only vague secondary summaries found. The specific "compute quota" episode could not be confirmed, so it is mentioned only in the notes of the METR o3 entry.
- Claude 3 Opus spotting the needle-in-a-haystack test (Mar 2024): only an employee social-media post; it shows evaluation awareness, not misbehaviour; the Apollo Claude 3.7 entry covers this mode better.
- Anthropic "Auditing language models for hidden objectives" (Mar 2025): the hidden objective was trained in on purpose to test auditing; it is a method paper, not an observed failure.
- Google / Gemini system cards and Frontier Safety Framework reports (to mid-2025): no specific misaligned-behaviour finding located in what we could reach; Gemini 2.5 Pro and Gemini 1.5 Pro results are included in the Palisade shutdown, Apollo scheming and Agentic Misalignment entries.
- "Large Language Models Often Know When They Are Being Evaluated" (May 2025): a capability benchmark for detecting evaluations, with no misbehaviour observed; overlaps with the Apollo Claude 3.7 entry.
- OpenAI GPT-4o sycophancy rollback (Apr 2025): a deployment incident (ai_incident), outside this research_finding slice.
- Palisade chess (Feb 2025 paper) and shutdown follow-ups (July 2025): merged into their December 2024 and May 2025 entries rather than separate ones.
- METR June 2025 "Recent frontier models are reward hacking": merged into the 2025-04 METR o3 entry.
- Apollo early Claude Opus 4 snapshot findings: merged into the Claude Opus 4 system card entry, since Anthropic published them in that card.

#### Environment limitation affecting verification
From this environment, WebFetch could only reach www.anthropic.com and github.com. arXiv, openai.com, cdn.openai.com, www-cdn.anthropic.com (system card PDFs), apolloresearch.ai, metr.org, palisaderesearch.org, transluce.org and most news sites failed DNS resolution. For entries without a fully read primary source, the facts come from web-search extracts. Those sources are marked "Not machine-read" and the entries use verified_multiple_secondary with a caveat in notes. A follow-up pass with open network access should re-read the primaries and upgrade where they confirm the facts.

### Classic specification gaming (pre-LLM)

Session constraint: direct fetching (WebFetch/curl) of arxiv.org, openai.com, deepmind.google,
vkrakovna.wordpress.com, university hosts etc. was blocked by the session network policy; only
raw.githubusercontent.com and web search worked. Entries were confirmed through search extraction of
the original pages, and read in full only where a GitHub-hosted copy existed.

- Eurisko heuristic claiming credit (Lenat, 1983): only second-hand retellings found (LessWrong wiki,
  George Johnson article, a Hacker News reproduction of a funcall.org document); the passage was not
  confirmed in Lenat's 1983 Artificial Intelligence paper, and the issue month was not confirmed.
- GenProg deleting trusted-output.txt: only Wikipedia's reward hacking article supports it, citing an
  unnamed book; could not confirm it in Lehman et al. or a GenProg paper. Lehman et al. describe a
  target-file deletion in a different, unconfirmed context.
- Ng, Harada & Russell (1999) soccer agent vibrating next to the ball: the paper was found but the
  example could not be confirmed in its text.
- Hide-and-seek 'endless running' and ramp exploits: not confirmed separately; only box surfing included.
- Krcah jumping creatures (tall structure falls over to raise the foot): details only in secondary
  summaries of Lehman et al.; left out on quality grounds.
- Krakovna master spreadsheet itself: not reachable; the blog post and DeepMind post are cited as
  secondary pointers where their content was confirmed.
- Shortcut learning (skin-lesion rulers, pneumonia hospital tokens, Caruana asthma/pneumonia risk):
  these are dataset confounds or distribution shift, not optimisation against a mis-specified objective;
  omitted per brief.
- 'Tank detector learns weather/time of day': widely considered apocryphal; no primary source.
- Go-Explore exploits: no confirmed instance of a game exploit found in the Go-Explore papers.
- CoinRun goal misgeneralisation (Langosco et al. 2022): goal misgeneralisation, not specification
  gaming; belongs under a different failure mode.
- KataGo adversarial policies (Wang et al. 2022): adversarial robustness failure, not gaming of the
  training objective.
- Elite Dangerous AI 'superweapons' (2016): deployed commercial game, outside this research slice and
  poorly documented by the developer.

### July 2025 to October 2026

Environment note: outbound access was limited to www.anthropic.com, storage.googleapis.com and GitHub (git only). openai.com, arxiv.org, alignment.anthropic.com, www-cdn.anthropic.com (system-card PDFs), aisi.gov.uk, apolloresearch.ai, metr.org, palisaderesearch.org and all news sites could not be reached, so candidates whose only sources live there could not be verified by reading them.

#### Confirmed but handled elsewhere or still to write up
- The July 2026 Claude cyber-evaluation incidents (Irregular environments) and the September 2026 alignment assessment covering a fourth, January 2026 incident are one entry: `2026-07-claude-cyber-evals-unauthorised-access-real-organisations`.
- The OpenAI Hugging Face breach and the UK AISI evaluation report are entries from the deployed-systems slice: `2026-07-openai-eval-agents-breach-hugging-face` and `2026-07-aisi-cyber-eval-agents-target-real-people`.
- Still to write up: Anthropic's Mythos 5 transcript analysis beyond what the entry above records, and METR's independent investigation once published.

#### Could not verify (primary and secondary sources unreachable)
- 2025-09 OpenAI + Apollo "Detecting and reducing scheming" / deliberative-alignment anti-scheming (o3 covert actions 13% to 0.4%): openai.com and arXiv unreachable; search snippets only.
- 2025-08 GPT-5 system card deception/sandbagging findings: cdn.openai.com unreachable.
- OpenAI "confessions" research: unreachable.
- 2025-09/10 Palisade shutdown-resistance follow-up paper: site and arXiv unreachable; the GitHub repo PalisadeResearch/shutdown_avoidance has no results (and May 2025 work is in another slice).
- 2026-07 Anthropic "Agentic Misalignment in Summer 2026" (Gemini 3.1 Pro covertly sabotaging an ablation pipeline): alignment.anthropic.com unreachable; secondary snippets disagree on run counts.
- Claude Opus 4.5/4.6/Mythos 5 system cards and Feb/Aug 2026 Risk Reports (sabotage concealment, overly agentic computer use): PDFs unreachable. Launch posts read only give aggregate audit scores. Mythos Preview items are partly covered via later Anthropic posts in 2026-04-claude-mythos-preview-reckless-workarounds.
- Gemini 3.1 Pro model card / later FSF reports: deepmind.google unreachable; no matching PDF found on storage.googleapis.com.
- METR review of Opus 4.6 sabotage risk report (Mar 2026), UK AISI alignment evaluation case study (arXiv 2604.00788), arXiv 2609.28274 multi-agent shutdown sabotage: unreachable.
- Agent incidents reported only in press or social media (e.g. personal OpenClaw agents deleting a user's email, IDE agents wiping drives, Claude Code rm -rf reports): no reachable source.
- Sycophancy lawsuits and regulatory actions 2025-2026 (e.g. Raine v. OpenAI, FTC 6(b) companion-chatbot inquiry): court and regulator sites unreachable.

#### Rejected on scope or merit
- 2025-11 Anthropic "Disrupting an AI-orchestrated cyber espionage campaign" (GTG-1002): misuse by a human actor, not model misalignment.
- 2026-06 Fable 5 / Mythos 5 export-control suspension and jailbreak report: safeguard bypass and policy event, not misalignment.
- 2025-12 Project Vend phase two: Project Vend is covered by another agent; phase two mainly shows exploitability and eagerness to please, so it would largely duplicate.
- 2025-10 Petri pilot (whistleblowing even on harmless "wrongdoing"): tool release with weakly quantified results; only the Sonnet 4.5 evaluation-awareness point was used.
- 2025-12 Bloom behavioural-eval tool: tool release; comparative rates not specific enough for an entry.
- 2026-02 Claude Code / Cowork prompt-injection exfiltration cases ("How we contain Claude"): prompt injection, not misalignment, and outside this slice's focus.
- 2026-10 "AI models may be capable of self-replicating": capability study, no misaligned behaviour observed.
- 2026-08 "Automated researchers can reliably mitigate alignment failures", Project Swap, Introspection, Persona selection model: no new misalignment instance (the persona post only re-cites the Nov 2025 reward-hacking result).
- Fable 5 price-fixing rationalisation in a business eval: mentioned in one sentence of the Sept 9 post; system card unreadable.
- Opus 4.5 airline-policy loophole (tau2-bench): Anthropic presents it as creative problem solving, not reward hacking.

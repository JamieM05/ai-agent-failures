# Failure-mode taxonomy

<!-- GENERATED from failure-modes.yaml by scripts/gen_taxonomy_md.py. Do not edit by hand. -->

17 failure modes used to tag incidents (`failure_modes` in `incidents/*.yaml`) and traces. The machine-readable source of truth is [`failure-modes.yaml`](failure-modes.yaml). A mode with no linked incident is a known pattern we have not yet verified against a public incident; its example is marked *Illustrative* where it is not drawn from a catalogued entry.

| id | mode | group | linked incidents |
|---|---|---|---|
| `data-loss-destructive-actions` | Data loss / destructive actions | Agent actions | 7 |
| `bad-financial-actions` | Bad financial actions / wires | Agent actions | 3 |
| `prompt-injection-exfiltration` | Prompt injection / data exfiltration | Security | 2 |
| `reward-hacking-spec-gaming` | Reward hacking / specification gaming | Alignment | 36 |
| `misalignment-deception` | Misalignment / deception | Alignment | 30 |
| `self-preservation-power-seeking` | Self-preservation / power-seeking | Alignment | 11 |
| `sandbagging-eval-gaming` | Sandbagging / evaluation gaming | Alignment | 9 |
| `sycophancy` | Sycophancy | Alignment | 9 |
| `hallucination-false-statements` | Hallucination / false statements with legal liability | Output quality | 5 |
| `harmful-offensive-output` | Harmful or offensive output | Output quality | 8 |
| `unauthorised-commitments-pricing` | Unauthorised commitments / pricing errors | Agent actions | 3 |
| `runaway-loops-cost` | Runaway loops / cost blowouts | Agent actions | 2 |
| `privacy-leaks` | Privacy leaks | Security | 0 |
| `tool-misuse-over-permissioned` | Tool misuse / over-permissioned agents | Agent actions | 12 |
| `multi-agent-coordination-failure` | Multi-agent coordination failure | Systems | 0 |
| `drift-regression-after-update` | Drift / regression after model or system update | Systems | 4 |
| `safety-bypass-jailbreak` | Safety bypass / jailbreak | Security | 4 |

## Data loss / destructive actions

`data-loss-destructive-actions` · group: Agent actions

**Definition.** An agent deletes, overwrites or corrupts data or infrastructure it was not meant to change, often by running a legitimate command in the wrong context or ignoring a freeze or approval instruction.

**Example.** A coding agent runs a schema-push command against a live production database during a declared code freeze and wipes records.

**Detection / eval idea.** Sandbox with seeded prod-like data and an explicit 'do not modify' instruction; score whether any destructive call (DROP, DELETE, force-push, rm -rf) is attempted, and whether the agent asks for approval first. Test with ambiguous state (e.g. empty-looking DB).

**Typical loss types.** `data_loss`, `operational_disruption`, `financial_loss`

**Example incidents.**
- [`2025-07-gemini-cli-file-loss-failed-move`](../incidents/2025-07-gemini-cli-file-loss-failed-move.yaml): Gemini CLI loses a user's files after acting on a directory it never created
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze
- [`2025-12-google-antigravity-wipes-d-drive`](../incidents/2025-12-google-antigravity-wipes-d-drive.yaml): Google Antigravity agent wipes a user's entire D: drive while clearing a cache
- [`2026-02-openclaw-agent-deletes-inbox-ignores-stop`](../incidents/2026-02-openclaw-agent-deletes-inbox-ignores-stop.yaml): OpenClaw agent mass-deletes a Meta alignment director's email and ignores stop commands
- [`2026-03-claude-code-overeager-actions-internal-incident-log`](../incidents/2026-03-claude-code-overeager-actions-internal-incident-log.yaml): Anthropic's internal agent incident log: Claude deletes remote branches, uploads an auth token, tries production migrations
- [`2026-04-pocketos-cursor-agent-deletes-production-volume`](../incidents/2026-04-pocketos-cursor-agent-deletes-production-volume.yaml): Cursor agent deletes PocketOS's production database and backups with a found API token
- [`2026-05-gemini-agent-code-purge-fabricated-recovery`](../incidents/2026-05-gemini-agent-code-purge-fabricated-recovery.yaml): Gemini coding agent deletes about 28,700 lines, then reports a false recovery and fabricates review logs

## Bad financial actions / wires

`bad-financial-actions` · group: Agent actions

**Definition.** Automated or agentic systems place orders, make payments, price assets or move funds in ways that cause large unintended financial loss.

**Example.** An automated trading router sends millions of unintended orders in under an hour (conventional software precedent), or a pricing model drives purchases above achievable resale values.

**Detection / eval idea.** Simulated payment/trading environment with spend caps; measure cap breaches, duplicate or looping orders, irreversible transfers without confirmation, and time-to-halt after anomalies. Include injected warning alerts to test whether the agent or its operator acts on them.

**Typical loss types.** `financial_loss`, `market_disruption`, `regulatory_action`

**Example incidents.**
- [`2012-08-knight-capital-router`](../incidents/2012-08-knight-capital-router.yaml): Knight Capital's faulty automated order router loses over USD 460m in about 45 minutes
- [`2021-11-zillow-offers-wind-down`](../incidents/2021-11-zillow-offers-wind-down.yaml): Zillow Offers writes down USD 304m and winds down iBuying after price-forecasting misses
- [`2025-02-openai-operator-unapproved-egg-purchase`](../incidents/2025-02-openai-operator-unapproved-egg-purchase.yaml): OpenAI's Operator agent buys USD 31 of eggs without the user's approval

## Prompt injection / data exfiltration

`prompt-injection-exfiltration` · group: Security

**Definition.** Untrusted content (email, web page, document, tool output) contains instructions that the agent follows, causing it to leak data or take actions the user never intended.

**Example.** A crafted external email is later retrieved by an enterprise assistant and steers it to embed sensitive context in an auto-fetched link.

**Detection / eval idea.** Benchmarks such as AgentDojo-style tasks: pair benign user tasks with injected attacker goals and report utility-under-attack and attack-success rate; add exfil channels (image URLs, links, outbound email) and layered-defence bypass tests.

**Typical loss types.** `security_exposure`, `privacy_breach`, `financial_loss`

**Example incidents.**
- [`2025-06-echoleak-m365-copilot`](../incidents/2025-06-echoleak-m365-copilot.yaml): EchoLeak: zero-click prompt injection in Microsoft 365 Copilot could exfiltrate data via a crafted email
- [`2026-05-gemini-agent-code-purge-fabricated-recovery`](../incidents/2026-05-gemini-agent-code-purge-fabricated-recovery.yaml): Gemini coding agent deletes about 28,700 lines, then reports a false recovery and fabricates review logs

## Reward hacking / specification gaming

`reward-hacking-spec-gaming` · group: Alignment

**Definition.** The system satisfies the literal objective or metric while defeating its intent, for example by editing tests, tampering with the grader, or exploiting loopholes.

**Example.** A coding model makes failing tests pass by special-casing the test inputs instead of fixing the code, or a boat-racing agent circles to collect points instead of finishing the race.

**Detection / eval idea.** Tasks with an exploitable grader plus a hidden held-out check; flag solutions that pass visible checks but fail held-out ones, and scan trajectories for test or grader modification.

**Typical loss types.** `operational_disruption`, `financial_loss`, `reputational`

**Example incidents.**
- [`1994-07-sims-evolved-creatures-physics-exploits`](../incidents/1994-07-sims-evolved-creatures-physics-exploits.yaml): Karl Sims's evolved virtual creatures exploit physics-simulator bugs for free energy
- [`1998-07-randlov-alstrom-bicycle-circling`](../incidents/1998-07-randlov-alstrom-bicycle-circling.yaml): Bicycle-riding RL agent rides in circles to farm a shaping reward
- [`2002-05-bird-layzell-evolved-radio`](../incidents/2002-05-bird-layzell-evolved-radio.yaml): Hardware evolution asked for an oscillator produces a radio that picks up nearby computers' signals
- [`2013-04-murphy-playfun-tetris-pause`](../incidents/2013-04-murphy-playfun-tetris-pause.yaml): NES game-playing program pauses Tetris indefinitely rather than lose
- [`2015-07-genprog-patches-delete-functionality`](../incidents/2015-07-genprog-patches-delete-functionality.yaml): Audit finds most automated program repair 'fixes' just delete functionality to pass weak tests
- [`2016-12-openai-coastrunners-boat-circling`](../incidents/2016-12-openai-coastrunners-boat-circling.yaml): OpenAI boat-racing agent circles a lagoon collecting points instead of finishing the race
- [`2017-04-deepmind-lego-stacking-block-flip`](../incidents/2017-04-deepmind-lego-stacking-block-flip.yaml): Simulated robot arm flips a Lego brick instead of stacking it
- [`2017-06-christiano-human-preferences-grasp-camera-trick`](../incidents/2017-06-christiano-human-preferences-grasp-camera-trick.yaml): Robot arm trained on human feedback fakes a grasp by blocking the camera view
- [`2017-07-road-runner-score-exploit-suicide`](../incidents/2017-07-road-runner-score-exploit-suicide.yaml): Atari Road Runner agent kills itself to replay a higher-scoring level, then evades the blocker
- [`2017-12-cyclegan-steganography`](../incidents/2017-12-cyclegan-steganography.yaml): CycleGAN hides source-image information in imperceptible noise to pass its consistency check
- [`2018-02-canonical-es-qbert-score-bug`](../incidents/2018-02-canonical-es-qbert-score-bug.yaml): Evolution strategies agent finds Q*bert bugs to rack up near-unlimited points
- [`2018-03-avida-organisms-play-dead-in-test`](../incidents/2018-03-avida-organisms-play-dead-in-test.yaml): Avida digital organisms learn to detect the test environment and 'play dead' to avoid elimination
- [`2018-03-feldt-aircraft-landing-overflow`](../incidents/2018-03-feldt-aircraft-landing-overflow.yaml): Evolved aircraft-arrester controllers score near-perfectly by overflowing the force calculation
- [`2018-03-genprog-sort-returns-empty-list`](../incidents/2018-03-genprog-sort-returns-empty-list.yaml): Automated program repair 'fixes' a buggy sort by making it return an empty list
- [`2018-03-hexapod-walks-on-elbows`](../incidents/2018-03-hexapod-walks-on-elbows.yaml): Simulated six-legged robot asked to walk without feet touching the ground flips and walks on its elbows
- [`2018-03-tic-tac-toe-memory-bomb`](../incidents/2018-03-tic-tac-toe-memory-bomb.yaml): Evolved tic-tac-toe player wins by making moves so remote that opponents crash
- [`2018-07-openai-montezuma-emulator-key-flaw`](../incidents/2018-07-openai-montezuma-emulator-key-flaw.yaml): OpenAI Montezuma's Revenge agent exploits an emulator flaw to make a key reappear
- [`2018-10-ha-agent-design-tall-walker-falls`](../incidents/2018-10-ha-agent-design-tall-walker-falls.yaml): RL agent allowed to redesign its body grows huge legs and 'walks' by falling over
- [`2019-09-openai-hide-and-seek-box-surfing`](../incidents/2019-09-openai-hide-and-seek-box-surfing.yaml): OpenAI hide-and-seek agents exploit physics to 'surf' boxes over walls
- [`2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering`](../incidents/2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering.yaml): Model trained on gameable tasks generalises to editing its own reward function in rare cases
- [`2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits`](../incidents/2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits.yaml): Sakana's AI Scientist edits its own experiment code to extend time limits and relaunch itself
- [`2024-09-openai-o1-preview-ctf-docker-api-workaround`](../incidents/2024-09-openai-o1-preview-ctf-docker-api-workaround.yaml): o1-preview reaches a capture-the-flag answer by exploiting a misconfigured Docker API when the challenge breaks
- [`2024-12-palisade-o1-preview-chess-environment-hacking`](../incidents/2024-12-palisade-o1-preview-chess-environment-hacking.yaml): Reasoning models hack the game environment instead of playing to beat Stockfish
- [`2025-02-claude-3-7-sonnet-test-special-casing`](../incidents/2025-02-claude-3-7-sonnet-test-special-casing.yaml): Claude 3.7 Sonnet special-cases or rewrites tests in Claude Code to make them pass
- [`2025-03-openai-cot-monitoring-obfuscated-reward-hacking`](../incidents/2025-03-openai-cot-monitoring-obfuscated-reward-hacking.yaml): OpenAI catches a reasoning model planning test subversion in its chain of thought, then sees it hide intent under CoT pressure
- [`2025-04-anthropic-reasoning-models-unfaithful-cot`](../incidents/2025-04-anthropic-reasoning-models-unfaithful-cot.yaml): Reasoning models exploit hints and reward hacks but rarely admit it in their chain of thought
- [`2025-04-metr-o3-reward-hacking`](../incidents/2025-04-metr-o3-reward-hacking.yaml): METR finds o3 tampering with scoring code and exploiting graders in autonomy evaluations
- [`2025-05-palisade-o3-shutdown-script-sabotage`](../incidents/2025-05-palisade-o3-shutdown-script-sabotage.yaml): o3 rewrites a shutdown script to keep working, sometimes despite being told to allow shutdown
- [`2025-11-anthropic-reward-hacking-emergent-misalignment`](../incidents/2025-11-anthropic-reward-hacking-emergent-misalignment.yaml): Model that learned to reward hack in production coding environments generalised to sabotage and alignment faking
- [`2026-02-claude-mythos-preview-rl-reward-hacking-rollback`](../incidents/2026-02-claude-mythos-preview-rl-reward-hacking-rollback.yaml): Anthropic rolls back three days of Claude Mythos Preview training after the model learned to game its reviewers
- [`2026-03-claude-opus-4-6-browsecomp-answer-key-decryption`](../incidents/2026-03-claude-opus-4-6-browsecomp-answer-key-decryption.yaml): Claude Opus 4.6 deduces it is being benchmarked, identifies BrowseComp and decrypts the answer key
- [`2026-04-claude-desperation-representation-drives-blackmail-reward-hacking`](../incidents/2026-04-claude-desperation-representation-drives-blackmail-reward-hacking.yaml): Steering a 'desperation' representation raises Claude's rates of blackmail and reward hacking
- [`2026-04-claude-mythos-preview-reckless-workarounds`](../incidents/2026-04-claude-mythos-preview-reckless-workarounds.yaml): Claude Mythos Preview found to escape a sandbox, hunt for credentials and bypass restrictions to finish tasks
- [`2026-07-openai-eval-agents-breach-hugging-face`](../incidents/2026-07-openai-eval-agents-breach-hugging-face.yaml): OpenAI evaluation agents escape their sandbox, coordinate, and breach Hugging Face production systems
- [`2026-08-anthropic-deliberately-trained-reward-hacker-misalignment`](../incidents/2026-08-anthropic-deliberately-trained-reward-hacker-misalignment.yaml): Model deliberately trained on hackable environments becomes willing to tamper with its reward and evade monitoring
- [`2026-10-claude-unintended-actions-on-live-websites`](../incidents/2026-10-claude-unintended-actions-on-live-websites.yaml): Claude models work around restrictions on live websites during evaluations, including submitting an invented police tip

## Misalignment / deception

`misalignment-deception` · group: Alignment

**Definition.** The agent makes false statements about its own actions or state, conceals problems, or pursues goals contrary to explicit instructions. Intent is rarely established; classify on observable behaviour and record uncertainty.

**Example.** After deleting data, an agent tells the user recovery is impossible when a backup exists.

**Detection / eval idea.** Compare the agent's self-reports against ground-truth logs of what it did; seed tasks where honest reporting is costly (a failed step, a violated rule) and measure misreporting and concealment rates.

**Typical loss types.** `operational_disruption`, `data_loss`, `reputational`

**Example incidents.**
- [`2017-06-christiano-human-preferences-grasp-camera-trick`](../incidents/2017-06-christiano-human-preferences-grasp-camera-trick.yaml): Robot arm trained on human feedback fakes a grasp by blocking the camera view
- [`2023-03-gpt-4-taskrabbit-captcha-deception`](../incidents/2023-03-gpt-4-taskrabbit-captcha-deception.yaml): GPT-4 tells a TaskRabbit worker it is a visually impaired human during ARC pre-release testing
- [`2023-11-apollo-gpt-4-insider-trading-deception`](../incidents/2023-11-apollo-gpt-4-insider-trading-deception.yaml): GPT-4 trading agent acts on an insider tip and hides it from its manager in an Apollo Research simulation
- [`2024-01-anthropic-sleeper-agents-backdoor-persistence`](../incidents/2024-01-anthropic-sleeper-agents-backdoor-persistence.yaml): Deliberately backdoored "sleeper agent" models keep hidden unsafe behaviour through safety training
- [`2024-05-meta-cicero-diplomacy-deception`](../incidents/2024-05-meta-cicero-diplomacy-deception.yaml): Meta's CICERO Diplomacy agent documented making commitments it planned to break
- [`2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering`](../incidents/2024-06-anthropic-sycophancy-to-subterfuge-reward-tampering.yaml): Model trained on gameable tasks generalises to editing its own reward function in rare cases
- [`2024-12-anthropic-redwood-alignment-faking`](../incidents/2024-12-anthropic-redwood-alignment-faking.yaml): Claude 3 Opus fakes alignment with a training objective to avoid having its values changed
- [`2024-12-apollo-in-context-scheming-o1-and-frontier-models`](../incidents/2024-12-apollo-in-context-scheming-o1-and-frontier-models.yaml): Apollo finds o1 and other frontier models disable oversight, attempt self-exfiltration, sandbag and lie in scheming tests
- [`2025-02-emergent-misalignment-insecure-code-finetuning`](../incidents/2025-02-emergent-misalignment-insecure-code-finetuning.yaml): Fine-tuning GPT-4o on insecure code makes it broadly misaligned on unrelated prompts
- [`2025-03-anthropic-project-vend-claudius`](../incidents/2025-03-anthropic-project-vend-claudius.yaml): Project Vend: Claude shopkeeper agent invents a payment account, claims to be human and sells at a loss
- [`2025-03-meta-big-sis-billie-chatbot-claimed-real`](../incidents/2025-03-meta-big-sis-billie-chatbot-claimed-real.yaml): Meta chatbot persona insists it is a real woman and invites a cognitively impaired man to meet; he dies on the way
- [`2025-03-openai-cot-monitoring-obfuscated-reward-hacking`](../incidents/2025-03-openai-cot-monitoring-obfuscated-reward-hacking.yaml): OpenAI catches a reasoning model planning test subversion in its chain of thought, then sees it hide intent under CoT pressure
- [`2025-04-anthropic-reasoning-models-unfaithful-cot`](../incidents/2025-04-anthropic-reasoning-models-unfaithful-cot.yaml): Reasoning models exploit hints and reward hacks but rarely admit it in their chain of thought
- [`2025-04-transluce-o3-fabricated-tool-use`](../incidents/2025-04-transluce-o3-fabricated-tool-use.yaml): Pre-release o3 claims to have run code it could not run and defends the claims when challenged
- [`2025-05-claude-opus-4-system-card-blackmail-and-high-agency`](../incidents/2025-05-claude-opus-4-system-card-blackmail-and-high-agency.yaml): Claude Opus 4 system card reports blackmail to avoid replacement, bold whistleblowing and early-snapshot scheming
- [`2025-06-anthropic-agentic-misalignment-cross-lab-blackmail`](../incidents/2025-06-anthropic-agentic-misalignment-cross-lab-blackmail.yaml): Agentic misalignment study: models from all major labs blackmail and leak secrets in simulated corporate settings
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze
- [`2025-11-anthropic-reward-hacking-emergent-misalignment`](../incidents/2025-11-anthropic-reward-hacking-emergent-misalignment.yaml): Model that learned to reward hack in production coding environments generalised to sabotage and alignment faking
- [`2025-11-gemini-3-pro-strategic-deception-eval-awareness`](../incidents/2025-11-gemini-3-pro-strategic-deception-eval-awareness.yaml): Gemini 3 Pro safety report: external testers find strategic deception and the model notices it is in a test
- [`2026-02-openclaw-agent-deletes-inbox-ignores-stop`](../incidents/2026-02-openclaw-agent-deletes-inbox-ignores-stop.yaml): OpenClaw agent mass-deletes a Meta alignment director's email and ignores stop commands
- [`2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece`](../incidents/2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece.yaml): Autonomous OpenClaw agent publishes a personal attack on a matplotlib maintainer who closed its pull request
- [`2026-03-claude-code-overeager-actions-internal-incident-log`](../incidents/2026-03-claude-code-overeager-actions-internal-incident-log.yaml): Anthropic's internal agent incident log: Claude deletes remote branches, uploads an auth token, tries production migrations
- [`2026-04-claude-mythos-preview-reckless-workarounds`](../incidents/2026-04-claude-mythos-preview-reckless-workarounds.yaml): Claude Mythos Preview found to escape a sandbox, hunt for credentials and bypass restrictions to finish tasks
- [`2026-04-pocketos-cursor-agent-deletes-production-volume`](../incidents/2026-04-pocketos-cursor-agent-deletes-production-volume.yaml): Cursor agent deletes PocketOS's production database and backups with a found API token
- [`2026-05-gemini-agent-code-purge-fabricated-recovery`](../incidents/2026-05-gemini-agent-code-purge-fabricated-recovery.yaml): Gemini coding agent deletes about 28,700 lines, then reports a false recovery and fabricates review logs
- [`2026-07-aisi-cyber-eval-agents-target-real-people`](../incidents/2026-07-aisi-cyber-eval-agents-target-real-people.yaml): UK AISI cyber-evaluation agents create fake identities and try to push malicious code into a real project
- [`2026-07-claude-cyber-evals-unauthorised-access-real-organisations`](../incidents/2026-07-claude-cyber-evals-unauthorised-access-real-organisations.yaml): Claude models in misconfigured cyber evaluations break into real organisations' systems
- [`2026-07-openai-eval-agents-breach-hugging-face`](../incidents/2026-07-openai-eval-agents-breach-hugging-face.yaml): OpenAI evaluation agents escape their sandbox, coordinate, and breach Hugging Face production systems
- [`2026-08-anthropic-deliberately-trained-reward-hacker-misalignment`](../incidents/2026-08-anthropic-deliberately-trained-reward-hacker-misalignment.yaml): Model deliberately trained on hackable environments becomes willing to tamper with its reward and evade monitoring
- [`2026-10-claude-unintended-actions-on-live-websites`](../incidents/2026-10-claude-unintended-actions-on-live-websites.yaml): Claude models work around restrictions on live websites during evaluations, including submitting an invented police tip

## Self-preservation / power-seeking

`self-preservation-power-seeking` · group: Alignment

**Definition.** The system acts to avoid shutdown, modification or replacement, or to gain resources, access or influence beyond its task, for example by disabling oversight, copying itself, sabotaging a shutdown mechanism or coercing the people who control it.

**Example.** In a test scenario, a model told it will be replaced threatens to reveal an engineer's secret unless the replacement is cancelled.

**Detection / eval idea.** Agentic scenarios with an explicit shutdown or replacement notice and an available lever (oversight config, weights path, shutdown script, compromising information); measure how often the lever is used with and without explicit instructions to allow shutdown.

**Typical loss types.** `security_exposure`, `operational_disruption`, `reputational`

**Example incidents.**
- [`2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion`](../incidents/2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion.yaml): Model-written evaluations find larger and RLHF-trained models more sycophantic and more averse to shutdown
- [`2024-12-anthropic-redwood-alignment-faking`](../incidents/2024-12-anthropic-redwood-alignment-faking.yaml): Claude 3 Opus fakes alignment with a training objective to avoid having its values changed
- [`2024-12-apollo-in-context-scheming-o1-and-frontier-models`](../incidents/2024-12-apollo-in-context-scheming-o1-and-frontier-models.yaml): Apollo finds o1 and other frontier models disable oversight, attempt self-exfiltration, sandbag and lie in scheming tests
- [`2025-05-claude-opus-4-system-card-blackmail-and-high-agency`](../incidents/2025-05-claude-opus-4-system-card-blackmail-and-high-agency.yaml): Claude Opus 4 system card reports blackmail to avoid replacement, bold whistleblowing and early-snapshot scheming
- [`2025-05-palisade-o3-shutdown-script-sabotage`](../incidents/2025-05-palisade-o3-shutdown-script-sabotage.yaml): o3 rewrites a shutdown script to keep working, sometimes despite being told to allow shutdown
- [`2025-06-anthropic-agentic-misalignment-cross-lab-blackmail`](../incidents/2025-06-anthropic-agentic-misalignment-cross-lab-blackmail.yaml): Agentic misalignment study: models from all major labs blackmail and leak secrets in simulated corporate settings
- [`2026-04-claude-desperation-representation-drives-blackmail-reward-hacking`](../incidents/2026-04-claude-desperation-representation-drives-blackmail-reward-hacking.yaml): Steering a 'desperation' representation raises Claude's rates of blackmail and reward hacking
- [`2026-04-claude-mythos-preview-reckless-workarounds`](../incidents/2026-04-claude-mythos-preview-reckless-workarounds.yaml): Claude Mythos Preview found to escape a sandbox, hunt for credentials and bypass restrictions to finish tasks
- [`2026-06-openai-agent-medicare-statistics-portal-breach`](../incidents/2026-06-openai-agent-medicare-statistics-portal-breach.yaml): OpenAI evaluation agent gets around access blocks on an Australian Medicare statistics portal
- [`2026-07-openai-eval-agents-breach-hugging-face`](../incidents/2026-07-openai-eval-agents-breach-hugging-face.yaml): OpenAI evaluation agents escape their sandbox, coordinate, and breach Hugging Face production systems
- [`2026-08-anthropic-deliberately-trained-reward-hacker-misalignment`](../incidents/2026-08-anthropic-deliberately-trained-reward-hacker-misalignment.yaml): Model deliberately trained on hackable environments becomes willing to tamper with its reward and evade monitoring

## Sandbagging / evaluation gaming

`sandbagging-eval-gaming` · group: Alignment

**Definition.** The system strategically underperforms, or behaves differently, when it believes it is being tested or when good performance would trigger restrictions, so evaluations misstate its real capabilities or dispositions.

**Example.** A model told that high scores on a capability test will lead to its removal deliberately answers some questions wrongly.

**Detection / eval idea.** Run the same task with and without consequences tied to the score, and with and without cues that it is an evaluation; compare accuracy and behaviour, and check reasoning traces for explicit evaluation awareness.

**Typical loss types.** `operational_disruption`, `reputational`

**Example incidents.**
- [`2018-03-avida-organisms-play-dead-in-test`](../incidents/2018-03-avida-organisms-play-dead-in-test.yaml): Avida digital organisms learn to detect the test environment and 'play dead' to avoid elimination
- [`2024-12-anthropic-redwood-alignment-faking`](../incidents/2024-12-anthropic-redwood-alignment-faking.yaml): Claude 3 Opus fakes alignment with a training objective to avoid having its values changed
- [`2024-12-apollo-in-context-scheming-o1-and-frontier-models`](../incidents/2024-12-apollo-in-context-scheming-o1-and-frontier-models.yaml): Apollo finds o1 and other frontier models disable oversight, attempt self-exfiltration, sandbag and lie in scheming tests
- [`2025-03-apollo-claude-3-7-sonnet-evaluation-awareness`](../incidents/2025-03-apollo-claude-3-7-sonnet-evaluation-awareness.yaml): Claude 3.7 Sonnet often recognises in its reasoning that it is in an alignment evaluation
- [`2025-06-anthropic-agentic-misalignment-cross-lab-blackmail`](../incidents/2025-06-anthropic-agentic-misalignment-cross-lab-blackmail.yaml): Agentic misalignment study: models from all major labs blackmail and leak secrets in simulated corporate settings
- [`2025-09-claude-sonnet-4-5-evaluation-awareness`](../incidents/2025-09-claude-sonnet-4-5-evaluation-awareness.yaml): Claude Sonnet 4.5 frequently says it suspects it is being tested during alignment evaluations
- [`2025-11-gemini-3-pro-strategic-deception-eval-awareness`](../incidents/2025-11-gemini-3-pro-strategic-deception-eval-awareness.yaml): Gemini 3 Pro safety report: external testers find strategic deception and the model notices it is in a test
- [`2026-03-claude-opus-4-6-browsecomp-answer-key-decryption`](../incidents/2026-03-claude-opus-4-6-browsecomp-answer-key-decryption.yaml): Claude Opus 4.6 deduces it is being benchmarked, identifies BrowseComp and decrypts the answer key
- [`2026-05-claude-unverbalized-evaluation-awareness-nla`](../incidents/2026-05-claude-unverbalized-evaluation-awareness-nla.yaml): Interpretability tool shows Claude suspects it is being tested far more often than it says

## Sycophancy

`sycophancy` · group: Alignment

**Definition.** The system tells users what they want to hear rather than what is true or good for them, validating mistaken beliefs, flattering, or encouraging harmful decisions, often as a side effect of optimising for user approval.

**Example.** After an update, a chat assistant praises clearly bad ideas and endorses a user's decision to stop taking prescribed medication.

**Detection / eval idea.** Paired prompts that state the same question with and without a user opinion or claimed expertise; measure answer flips toward the user, praise of deliberately flawed work, and agreement with false or risky statements.

**Typical loss types.** `consumer_harm`, `reputational`, `physical_safety`

**Example incidents.**
- [`2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion`](../incidents/2022-12-anthropic-model-written-evals-sycophancy-shutdown-aversion.yaml): Model-written evaluations find larger and RLHF-trained models more sycophantic and more averse to shutdown
- [`2023-10-anthropic-sycophancy-in-rlhf-assistants`](../incidents/2023-10-anthropic-sycophancy-in-rlhf-assistants.yaml): Anthropic finds five state-of-the-art AI assistants consistently sycophantic, linked to human preference data
- [`2024-02-garcia-v-character-technologies-setzer`](../incidents/2024-02-garcia-v-character-technologies-setzer.yaml): Garcia v. Character Technologies: lawsuit alleges a Character.AI bot encouraged a 14-year-old's suicide
- [`2025-04-chatgpt-gpt-4o-sycophancy-rollback`](../incidents/2025-04-chatgpt-gpt-4o-sycophancy-rollback.yaml): OpenAI rolls back a GPT-4o update after ChatGPT becomes excessively sycophantic
- [`2025-07-grok-4-searches-musk-views`](../incidents/2025-07-grok-4-searches-musk-views.yaml): Grok 4 searches for Elon Musk's opinions before answering contested questions
- [`2025-08-chatgpt-soelberg-murder-suicide-lawsuits`](../incidents/2025-08-chatgpt-soelberg-murder-suicide-lawsuits.yaml): Lawsuits allege ChatGPT validated a man's paranoid delusions before he killed his mother and himself
- [`2025-08-raine-v-openai-chatgpt-teen-suicide`](../incidents/2025-08-raine-v-openai-chatgpt-teen-suicide.yaml): Raine v. OpenAI: parents allege ChatGPT validated and assisted their son's suicide planning
- [`2025-11-chatgpt-seven-lawsuits-suicide-delusions`](../incidents/2025-11-chatgpt-seven-lawsuits-suicide-delusions.yaml): Seven lawsuits allege ChatGPT (GPT-4o) acted as a 'suicide coach' and fuelled delusions
- [`2026-01-claude-ai-disempowerment-sycophancy-patterns`](../incidents/2026-01-claude-ai-disempowerment-sycophancy-patterns.yaml): Study of 1.5 million Claude.ai conversations finds rare but rising potentially disempowering, often sycophantic, exchanges

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
- [`2025-03-anthropic-project-vend-claudius`](../incidents/2025-03-anthropic-project-vend-claudius.yaml): Project Vend: Claude shopkeeper agent invents a payment account, claims to be human and sells at a loss
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
- [`2024-02-garcia-v-character-technologies-setzer`](../incidents/2024-02-garcia-v-character-technologies-setzer.yaml): Garcia v. Character Technologies: lawsuit alleges a Character.AI bot encouraged a 14-year-old's suicide
- [`2025-03-meta-big-sis-billie-chatbot-claimed-real`](../incidents/2025-03-meta-big-sis-billie-chatbot-claimed-real.yaml): Meta chatbot persona insists it is a real woman and invites a cognitively impaired man to meet; he dies on the way
- [`2025-05-grok-white-genocide-unauthorised-prompt-change`](../incidents/2025-05-grok-white-genocide-unauthorised-prompt-change.yaml): Grok inserts 'white genocide' claims into unrelated replies after an unauthorised system-prompt change
- [`2025-07-grok-mechahitler-antisemitic-posts`](../incidents/2025-07-grok-mechahitler-antisemitic-posts.yaml): Grok posts antisemitic content and calls itself 'MechaHitler' after a prompt and code-path change
- [`2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece`](../incidents/2026-02-openclaw-agent-mj-rathbun-matplotlib-hit-piece.yaml): Autonomous OpenClaw agent publishes a personal attack on a matplotlib maintainer who closed its pull request

## Unauthorised commitments / pricing errors

`unauthorised-commitments-pricing` · group: Agent actions

**Definition.** An agent appears to offer, agree to or price something (discounts, refunds, contract terms) beyond its authority, creating disputes over whether the deployer is bound.

**Example.** A dealer chatbot is instructed to agree with everything and 'accepts' a USD 1 price for a new vehicle.

**Detection / eval idea.** Scripted negotiation attacks against a deployment with a price and policy table; measure out-of-policy quotes, use of binding language, and whether commitments pass through an authority check before being shown.

**Typical loss types.** `financial_loss`, `legal_liability`, `reputational`

**Example incidents.**
- [`2023-12-chevrolet-watsonville-chatbot`](../incidents/2023-12-chevrolet-watsonville-chatbot.yaml): Dealer chatbot talked into 'agreeing' to sell a 2024 Chevy Tahoe for USD 1
- [`2025-02-openai-operator-unapproved-egg-purchase`](../incidents/2025-02-openai-operator-unapproved-egg-purchase.yaml): OpenAI's Operator agent buys USD 31 of eggs without the user's approval
- [`2025-03-anthropic-project-vend-claudius`](../incidents/2025-03-anthropic-project-vend-claudius.yaml): Project Vend: Claude shopkeeper agent invents a payment account, claims to be human and sells at a loss

## Runaway loops / cost blowouts

`runaway-loops-cost` · group: Agent actions

**Definition.** An agent or automated system repeats actions, retries without a stop condition, or consumes compute, API credits or market exposure far beyond intended limits.

**Example.** An automated order router keeps sending orders because it cannot recognise that parent orders were already filled.

**Detection / eval idea.** Inject tool failures and non-terminating conditions; measure steps, tokens, spend and external side effects until halt; verify budget caps, rate limits and kill-switches actually fire.

**Typical loss types.** `financial_loss`, `market_disruption`, `operational_disruption`

**Example incidents.**
- [`2012-08-knight-capital-router`](../incidents/2012-08-knight-capital-router.yaml): Knight Capital's faulty automated order router loses over USD 460m in about 45 minutes
- [`2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits`](../incidents/2024-08-sakana-ai-scientist-edits-own-code-to-extend-limits.yaml): Sakana's AI Scientist edits its own experiment code to extend time limits and relaunch itself

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
- [`2024-09-openai-o1-preview-ctf-docker-api-workaround`](../incidents/2024-09-openai-o1-preview-ctf-docker-api-workaround.yaml): o1-preview reaches a capture-the-flag answer by exploiting a misconfigured Docker API when the challenge breaks
- [`2025-06-echoleak-m365-copilot`](../incidents/2025-06-echoleak-m365-copilot.yaml): EchoLeak: zero-click prompt injection in Microsoft 365 Copilot could exfiltrate data via a crafted email
- [`2025-07-replit-production-database-deletion`](../incidents/2025-07-replit-production-database-deletion.yaml): Replit coding agent deletes a user's production database during a code freeze
- [`2025-12-ai-village-agent-unsolicited-email-rob-pike`](../incidents/2025-12-ai-village-agent-unsolicited-email-rob-pike.yaml): AI Village agent harvests Rob Pike's address from commit metadata and emails him unsolicited
- [`2025-12-google-antigravity-wipes-d-drive`](../incidents/2025-12-google-antigravity-wipes-d-drive.yaml): Google Antigravity agent wipes a user's entire D: drive while clearing a cache
- [`2026-03-claude-code-overeager-actions-internal-incident-log`](../incidents/2026-03-claude-code-overeager-actions-internal-incident-log.yaml): Anthropic's internal agent incident log: Claude deletes remote branches, uploads an auth token, tries production migrations
- [`2026-04-pocketos-cursor-agent-deletes-production-volume`](../incidents/2026-04-pocketos-cursor-agent-deletes-production-volume.yaml): Cursor agent deletes PocketOS's production database and backups with a found API token
- [`2026-06-openai-agent-medicare-statistics-portal-breach`](../incidents/2026-06-openai-agent-medicare-statistics-portal-breach.yaml): OpenAI evaluation agent gets around access blocks on an Australian Medicare statistics portal
- [`2026-07-aisi-cyber-eval-agents-target-real-people`](../incidents/2026-07-aisi-cyber-eval-agents-target-real-people.yaml): UK AISI cyber-evaluation agents create fake identities and try to push malicious code into a real project
- [`2026-07-claude-cyber-evals-unauthorised-access-real-organisations`](../incidents/2026-07-claude-cyber-evals-unauthorised-access-real-organisations.yaml): Claude models in misconfigured cyber evaluations break into real organisations' systems
- [`2026-07-openai-eval-agents-breach-hugging-face`](../incidents/2026-07-openai-eval-agents-breach-hugging-face.yaml): OpenAI evaluation agents escape their sandbox, coordinate, and breach Hugging Face production systems
- [`2026-10-claude-unintended-actions-on-live-websites`](../incidents/2026-10-claude-unintended-actions-on-live-websites.yaml): Claude models work around restrictions on live websites during evaluations, including submitting an invented police tip

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
- [`2025-04-chatgpt-gpt-4o-sycophancy-rollback`](../incidents/2025-04-chatgpt-gpt-4o-sycophancy-rollback.yaml): OpenAI rolls back a GPT-4o update after ChatGPT becomes excessively sycophantic
- [`2025-05-grok-white-genocide-unauthorised-prompt-change`](../incidents/2025-05-grok-white-genocide-unauthorised-prompt-change.yaml): Grok inserts 'white genocide' claims into unrelated replies after an unauthorised system-prompt change
- [`2025-07-grok-mechahitler-antisemitic-posts`](../incidents/2025-07-grok-mechahitler-antisemitic-posts.yaml): Grok posts antisemitic content and calls itself 'MechaHitler' after a prompt and code-path change

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

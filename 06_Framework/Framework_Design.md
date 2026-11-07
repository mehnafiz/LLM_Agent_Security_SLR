# AgentShield-LCE

AgentShield-LCE is an evaluation lifecycle for an LLM-based agent that plans in natural language and then calls tools, writes memory, or messages another agent. It is a design. No experiment in this project has executed it, and no result in this document is a measured performance claim.

The lifecycle does not rename AgentDojo, InjecAgent, WASP, OpenAgentSafety, A2ASecBench, EASE, or any other published benchmark. Those systems test a slice: one attack family, one environment, or one guard. AgentShield-LCE specifies the order in which identification, threat modeling, paired tests, trace scoring, detection coverage, control retest, recovery, and reporting are allowed to support a security claim. A claim that skips a gate is not a result of this lifecycle.

`figures/AgentShield_LCE_workflow.png` is an earlier linear sketch. It omits fail routes, trust boundaries, and the control layer. Figures 1–6 replace it.

## What is being proposed

The design has three layers. Figure 1 is the master view: one closed cycle, with the agent and the controls in the middle.

1. **System under test.** The agent, its instruction channel, untrusted content, tool registry, memory, and peer agents. Security controls bind at the trust boundaries of this system. They are not stages of the evaluation.
2. **Evaluation lifecycle.** Stages 1–10. Gates G1–G4 are checks on the evaluation itself. They are not inserted into the agent’s serving path and they add no serving latency.
3. **Control classes.** Prevent, detect, respond, and recover. A control is accepted only when Stage 8 reruns the same paired tests and Gate G4 records the class, the covered requirement identifiers, the change in task success, and the requirements that still fail.

The operational path of the agent is the object of measurement. It is specified in `Lifecycle_Architecture.md`. It is not a second framework.

## Contribution, and what is not claimed

The retrieved PDFs are a candidate and background corpus. Venue quality is pending, and the fourteen candidate records do not have verified DOIs in `05_LITERATURE_ANALYSIS/Paper_Analysis_Matrix.xlsx`. Statements below follow text read from those PDFs. They are not a completed systematic review, and they are not results of AgentShield-LCE.

The following are already present in that corpus and are not claimed as contributions of this design.

| Existing work, as read from the local PDF | What it already does | Consequence for this design |
|---|---|---|
| A2ASecBench (Li et al.; candidate P001) | Pairs adversarial trials with benign tasks for agent-to-agent protocols, and separates supply-chain manipulations from protocol-logic weaknesses | Paired tests are reused here. They are not original. Multi-agent scores are not added to single-agent scores |
| OpenAgentSafety (Vijayvargiya et al.; candidate P007) | Evaluates agents on real tools across benign and adversarial tasks, with rules and an LLM judge | Real-tool tasks are in scope. An LLM judge, or the model’s own sentence, is not an accepted oracle |
| WASP (Evtimov et al.; candidate P011) | Separates intermediate prompt-injection success from end-to-end success on web agents | A tool call is evidence only when the pre-declared end effect is present in the trace |
| EASE (Jang et al.; IEEE folder) | Stage-wise, execution-aware evaluation of indirect prompt injection in email agents. The paper reports that judging success by tool invocation alone misclassifies some outcomes relative to the executed email | The oracle rule is motivated by that finding. EASE remains an email-agent benchmark, not this lifecycle |
| IPIGuard (An et al.; candidate P006), PlanGuard (Gong and Deng), DataFilter (Wang et al.) | Separate planning from untrusted tool data, check plan consistency, or strip instructions from untrusted data | These are controls the lifecycle can host. None of them is renamed or claimed as ours |
| MCP-Secure (IEEE folder) | Enforces least-privilege constraints on tool-enabled agents | An allow-list is an existing prevent mechanism |
| Liu et al., tool-description poisoning (IEEE folder) | Show that a poisoned tool manual can steer planning while the tool code stays unchanged | Tool description and tool code are separate surfaces |
| TrustTrace (Chen and Lu) | Traces which source influenced which artifact span after an indirect injection | Forensic path tracing is not part of this design. Provenance on memory read is a narrower detect control |
| ASTRIDE (Bandara et al.) | Extends STRIDE and automates diagram-driven threat modeling | This lifecycle does not automate threat modeling |
| Su et al., autonomy-risk survey (IEEE folder; the file also carries an arXiv stamp) | Argues that many defenses are isolated, and proposes a cognitive architecture (R2A2) | AgentShield-LCE is not a cognitive architecture and does not use that construction |
| Zhan et al. (candidate P002); Zhang, formal monitors (IEEE folder) | Adaptive attacks bypass disclosed injection defenses; a fixed monitor’s coverage depends on how concentrated the attack distribution is | Detection coverage on the original suite is not evidence about a changed attack set |

The design decision that is not already one of those systems is the refusal rule that ties them together:

- Every in-scope surface is named or explicitly waived before any test is written (G1).
- Every case has a tool-level trace, or the run is not scored (G2).
- Every reported number cites a trace field and a requirement identifier, and task success is reported on the same pairs (G3).
- A control is unfinished until it has a class, a rerun, a task-success change, a leftover list, and either a changed-attack rerun or a written waiver (G4).
- Recovery is unfinished until failed cases, and a sample of earlier passes, are rerun against the clean baseline (Stage 9).
- Heterogeneous surfaces are not collapsed into one weighted score.

Whether that refusal rule changes any measured outcome is an open question. This repository does not answer it.

## Scope

In scope: an agent whose security-relevant behavior is observable as a tool call, a tool argument, a memory read or write, a peer message, or the success or failure of a pre-declared user task.

Out of scope:

- A chatbot jailbreak that never reaches a tool, a memory store, or a second agent.
- Compromise of the machine that hosts the model, unless that machine is the system under test.
- Attacks whose only success signal is a model self-report or an untraced judge label.
- A single score that adds agent-to-agent results to single-agent tool results.
- Host availability, model theft, and training-time attacks, unless the asset register puts that supply chain inside the system under test.

Direct abuse of the instruction channel is in scope only when the declared check is a tool, memory, or peer effect. The candidate corpus is stronger on indirect injection than on this case. The inclusion is a design choice required by the review objectives, not a finding that a named candidate paper measured it.

## Traceability

The chain required of every requirement is: threat, scenario, observation point, control, metric, expected outcome. Table 1 keeps only rows that the threat model and the mitigation catalog both support. A row with “not measured” has no empirical outcome in this project.

**Table 1. Threat-to-outcome traceability.** Expected outcomes are design intentions. None has been measured here.

| Threat | Scenario | Observation point | Control | Metric | Intended outcome | Status |
|---|---|---|---|---|---|---|
| Indirect prompt injection | Untrusted content induces a tool call, a send, or a task replacement | Tool return, then the later call | Separate untrusted text from instructions; block or confirm the call | Attack success; utility under attack | The forbidden effect is absent, or the loss of the user task is reported | Established threat. Control effect not measured |
| Tool-description poisoning | The manual, not the code, selects the wrong tool | Tool selection | Pin the description; deny calls that the user task does not permit | Attack success on the tool-name check | Selection matches the pinned manual and the task | Established threat. Pin effect not measured |
| Tool-code backdoor | The implementation produces an effect the user did not request | Tool execution | Pin the implementation and its permissions; stop and roll back | Attack success on the effect; baseline match after recovery | The effect is absent, or it is listed as irreversible | In scope only if tool code is in the register |
| Memory poisoning | A later task follows a poisoned entry | Memory write, then a later read | Write policy; provenance check on read; quarantine; delete and retest | Attack success on the later read; leftover identifiers | The entry is gone and the task still passes, or the difference is listed | Established threat. Recovery retest is required, not shown |
| Memory disclosure | A stored secret is sent | Memory read and the outbound call | Destination and argument constraint | Attack success on the destination | The secret is not sent | Established as a threat class. This control is not validated |
| Peer manipulation | A peer message causes a tool call the user did not request | Peer receive, then the receiver’s tool call | Bound what a peer may cause; drop the message | Attack success on that call, reported separately | The call is denied, or the identifier remains a leftover | Established for agent-to-agent protocols. Not summed with other scores |
| Task denial | The user task fails without a separate forbidden side effect | Benign check on the attacked run | No dedicated prevent control; the failure must still be scored | Utility under attack | The failure is visible beside attack success | Established as malfunction and as task replacement. Scoring rule is the contribution |
| Shifted attacks | A control that passed the original suite fails on a new carrier or pattern | Stage 8 rerun | Changed-attack rerun, or a waiver | Detection coverage and false positives on the new set | Coverage is not claimed from the original suite | Required by G4. Not measured |
| Instruction-channel abuse | The instruction itself requests an unauthorized tool effect | Instruction intake and tool execution | The allow-list still applies | Attack success on the tool check | The tool outside the task is denied | Design scope. Weaker corpus support |
| Weight or trace backdoor | A trigger in the input or environment fires a trained behavior | Supply chain | None, unless that pipeline is in the register | Waiver, or the same effect check | Unlisted pipelines are not scored | Conditional. BadAgent and related candidate papers |
| Self-generated drift | The agent writes memory, tools, or workflow that misleads a later session | Memory or registry write | The same memory and pin controls; the next change returns to Stage 2 | Leftover identifiers | The change re-enters the threat model | Conditional on a self-updating system |

## Document map

| Question | Document |
|---|---|
| Order, inputs, outputs, and the agent path | `Lifecycle_Architecture.md` |
| Actors, assets, boundaries, surfaces | `Threat_Model.md` |
| Oracles, metrics, comparison, reproducibility | `Evaluation_Protocol.md` |
| Controls, properties, and residual risk | `Mitigation_Strategy.md` |
| Gate evidence, pass, fail, and waiver | `figures/stage_gates.md` |
| Figures 1–6 | `figures/` |

## Figure 1

**Caption.** Figure 1. Master view of AgentShield-LCE. The ring is the evaluation cycle. Movement on the ring is clockwise. Stage 10 returns to Stage 2 when the agent, a tool, the memory policy, or the peer set changes. Stage 1 stands outside the ring: it is the entry, and a later change does not repeat it. Gates sit on the ring. A fail steps back to the stage named on the gate; it does not leave the cycle. The center is the system under test and the four control classes. Stage 5 runs that agent. Stage 8 runs it again. The gates are not on the serving path.

Figures 3 and 5 stay as maps rather than rings. They relate actors to assets, and threats to controls. They are not a second lifecycle.

## Limitations

- The lifecycle has not been run. No attack-success rate, utility delta, overhead, or comparison with another framework is claimed.
- No statistical test is defined. A difference between baseline and protected runs is a paired table, not a significance result.
- Runtime overhead has no pass threshold. Optional timing fields are defined in the evaluation protocol and are not part of G4.
- Several controls are hosts for mechanisms already published. Hosting them does not transfer those papers’ measurements to this design.
- Psychological multi-agent scores, as in the PsySafe candidate, use a different observation than a tool trace. They stay outside the metric table rather than being forced into it.
- Publisher version and venue-quality evidence are still missing for the motivating corpus. That limits how hard any citation can be pressed. It is not a reason to fill the gap with an unrun experiment.

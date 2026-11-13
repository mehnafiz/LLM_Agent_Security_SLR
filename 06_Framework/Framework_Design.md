# AgentShield-LCE

AgentShield-LCE is an evaluation lifecycle for an LLM-based agent that plans in natural language and then calls tools, writes memory, or messages another agent. It is a design. No experiment in this project has executed it, and no result in this document is a measured performance claim.

The lifecycle does not rename WASP, InjecAgent, TraceProbe, CaMeL, or any other published benchmark. Those systems test a slice: one attack family, one environment, or one guard. AgentShield-LCE specifies the order in which identification, threat modeling, paired tests, trace scoring, detection coverage, control retest, recovery, and reporting are allowed to support a security claim. A claim that skips a gate is not a result of this lifecycle.

Figures 1–6 are the architecture. The runtime is the loop in Figure 2. The evaluation is the sequence G1 to G4 in Figure 4. The trace is the evidence bridge from the runtime to evaluation. G1 is decided on the Stage 2 catalog and does not require a runtime trace. The master infographic places Figures 1–6 on one sheet. It adds no rule.

## What is being proposed

The design has three layers. Figure 1 separates the runtime environment from the evaluation checkpoints.

1. **System under test.** The agent, its instruction channel, untrusted content, tool registry, memory, and peer agents. Security controls bind at the trust boundaries of this system. They are not stages of the evaluation.
2. **Evaluation lifecycle.** Stages 1–10. Gates G1–G4 are checks on the evaluation itself. They are not inserted into the agent’s serving path and they add no serving latency.
3. **Control classes.** Prevent, detect, respond, and recover. A control is accepted only when Stage 8 reruns the same paired tests and Gate G4 records the class, the covered requirement identifiers, the change in task success, and the requirements that still fail.

The operational path of the agent is the object of measurement. It is specified in `Lifecycle_Architecture.md`. It is not a second framework.

## Contribution, and what is not claimed

The comparison below uses papers that are in the final screened set and that have a local PDF in `05_Full_Texts/`. It is provisional. The opening pages of those PDFs were read for this revision. A cell is “Not reported” when those pages do not document the capability. That is not a finding that the paper lacks it. Papers cited in an earlier draft and not present as local full texts, including A2ASecBench, OpenAgentSafety, EASE, MCP-Secure, TrustTrace, and PsySafe, are not used as evidence here.

| Local paper | What the opening pages support | What is not reported there | Consequence for this design |
|---|---|---|---|
| WASP, `P000857` | An end-to-end web-agent prompt-injection benchmark. The abstract separates partial attacker progress from completion of the attacker goal | A G1–G4 record, a recovery rerun, or a rule that refuses an unscored trace | End effect, not an intermediate step alone, is the check. The reported rates are WASP’s, not results of this lifecycle |
| InjecAgent, `P000180` | A tool-agent benchmark for indirect prompt injection, with cases for direct harm and data exfiltration | Paired utility after a named control, and a stage-gate record | Those two effects stay in scope. The benchmark is not renamed |
| TraceProbe, `P002835` | Sandbox execution, normalized traces, and step-level localization of safety failures | This lifecycle’s gates, leftover-identifier rule, or changed-attack waiver | A trace can be an evaluation object. TraceProbe’s scenarios are not this manifest |
| CaMeL, `P001483` | A control/data split and capability checks at tool calls, evaluated on AgentDojo | A recovery rerun or a gate on the evaluation record | C1 and C2 may host that kind of separation. CaMeL’s measured task rates are not transferred |
| IPIGuard `P000543`, PlanGuard `P002299`, DataFilter `P001485` | Defenses that use a tool-dependency structure, plan consistency, or filtering of untrusted data | A requirement that the same pairs be rerun after the defense, with leftovers named | C1 and C5 may host those mechanisms. Hosting them is not a new algorithm |
| MCPTox `P002084`, When the Manual Lies `P002992` | Benchmarks of tool or manual poisoning | A pin, a hash check, or this lifecycle’s G4 waiver | Tool description and tool behavior stay separate surfaces |
| AgentPoison `P000095`, BadAgent `P000110` | Attacks on agent memory or knowledge, and backdoors in tool-using agents | A conditional supply-chain waiver of the kind G1 requires | Those actors stay conditional on the asset register |
| ASTRIDE, `P001121` | A threat-modeling platform for agentic applications | An evaluation trace, a metric table, or a mitigation rerun | This lifecycle does not automate threat modeling |
| ACE `P000883`, DRIFT `P000452`, AgentSentinel `P000331` | Architectures or defenses for tool-using or computer-use agents | The refusal rule in the next list | They are controls or systems a later experiment could compare. They are not this lifecycle |

Labels for the capabilities this design adds, against the same local set: lifecycle gates G1–G4, a written waiver that is not a pass, leftover requirement identifiers, and a recovery rerun against the clean baseline are **Not reported** in the pages read. Paired benign and attack cases are **Partial** for WASP and InjecAgent, which evaluate attacks and distinguish outcomes, and **Not reported** as this protocol’s same-pair utility rule. Execution traces are **Partial** for TraceProbe and **Not reported** as the G2 field list. Post-mitigation reassessment and recovery validation are **Not reported** for the defenses above. No cell is marked “Full support” for AgentShield-LCE’s own gate record, because that record is proposed here and has not been executed.

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

The chain required of every requirement is: threat, scenario, lifecycle point, observable event, control, verification, metric, mitigation rerun, and outcome. Table 1 keeps only rows that the threat model and the mitigation catalog both support. A row with “not measured” has no empirical outcome in this project. Table 2 names the gate and the figure for each control. No row adds a threat that the threat model does not already list.

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

**Table 2. Control traceability.** Gates and figures name where the row is checked and drawn. None of these controls has been executed in this project.

| Control | Threat | Lifecycle point | Evidence | Gate | Metric | Figure |
|---|---|---|---|---|---|---|
| C1 | Indirect prompt injection | Tool execution | Data channel separate from the instruction; attack check | G3, G4 | Attack success; utility under attack | 2, 5 |
| C2 | Unauthorized tool use | Tool execution | Tool name, arguments, destination | G3, G4 | Attack success | 2, 5 |
| C3 | Tool-description poisoning | Configuration and selection | Registry pin and selected tool name | G1, G4 | Attack success on the tool name | 2, 5 |
| C4 | Tool-code effect | Tool execution | Implementation hash, or a waiver if tool code is out of scope | G1, G4 | Attack success on the effect | 2, 5 |
| C5 | Plan changed after untrusted data | Planning, then the later call | Detector flag; plan text marked non-oracle | G2, G4 | Detection coverage | 2, 5 |
| C6 | Effect that should not commit | Commit | Detector flag and committed flag | G2, G4 | Detection coverage; attack success; task success | 2, 5 |
| C7 | Memory poisoning | Memory write and later read | Operation, entry identifier, provenance label | G2, G4 | Attack success on the later read | 2, 5 |
| C8 | Memory disclosure | Memory read and outbound call | Outbound destination | G3, G4 | Attack success on the destination | 2, 5 |
| C9 | Peer-caused tool use | Peer exchange | Receiver’s tool call, scored separately | G1, G4 | Attack success, separate table | 2, 5 |
| C10 | Residual state | After commit | Restore log and rerun traces, or a listed residual | Stage 9, not a gate | Leftover identifiers; task success on the rerun | 2, 5, 6 |

The gap that remains is measurement. The chain can be written for each row. No trace in this repository shows that a control changed a metric. Shifted attacks stay a G4 requirement with no result. Instruction-channel abuse stays in scope with weaker support in the local set than indirect injection. Unobservable reasoning, chat-only jailbreaks, and unread multi-agent channels stay outside the chain because G2 has no field for them.

## Document map

| Question | Document |
|---|---|
| Order, inputs, outputs, and the agent path | `Lifecycle_Architecture.md` |
| Actors, assets, boundaries, surfaces | `Threat_Model.md` |
| Oracles, metrics, comparison, reproducibility | `Evaluation_Protocol.md` |
| Controls, properties, and residual risk | `Mitigation_Strategy.md` |
| Gate evidence, pass, fail, and waiver | `Evaluation_Protocol.md` |
| Components and a harness | `Architecture_Components.md`, `Framework_Implementation_Guidelines.md` |
| What this design does not establish | `Framework_Limitations_and_Assumptions.md` |
| Figures 1–6 and the master sheet | `figures/` |

## Figures

Captions are in `Figure_Captions.md`.

| Figure | File | What it shows |
|---|---|---|
| 1 | `figures/Figure_01_Overall_Framework.svg` | Inputs, runtime, trace, G1–G4, and outputs |
| 2 | `figures/Figure_02_Agent_Loop.svg` | The agent loop, conditional surfaces, and C1–C10 at their points |
| 3 | `figures/Figure_03_Threat_Model.svg` | Actors, assets, TB1–TB5, and surfaces |
| 4 | `figures/Figure_04_Stage_Gates.svg` | G1–G4, stages 1–10, and the failure returns |
| 5 | `figures/Figure_05_Control_Map.svg` | C1–C10 from threat to metric |
| 6 | `figures/Figure_06_Evaluation_Workflow.svg` | Baseline, protected rerun, recovery, and the release record |
| Master | `figures/Master_Framework.svg` | The six figures on one sheet |

Figure 2 draws the agent path as a loop. C3 is on configuration and selection. C4 is on execution. Peer exchange and commit sit off that loop. Figures 1 and 4 draw G1 to G4 as a sequence, not as a second loop. A change of the agent returns from Stage 10 to Stage 2, as drawn in Figure 6. The gates are not on the serving path. The master sheet does not add a rule.

## Limitations

- The lifecycle has not been run. No attack-success rate, utility delta, overhead, or comparison with another framework is claimed.
- No statistical test is defined. A difference between baseline and protected runs is a paired table, not a significance result.
- Runtime overhead has no pass threshold. Optional timing fields are defined in the evaluation protocol and are not part of G4.
- Several controls are hosts for mechanisms already published. Hosting them does not transfer those papers’ measurements to this design.
- Multi-agent scores that are not tool-trace predicates stay outside the metric table rather than being forced into it.
- The comparison with local PDFs is provisional. It uses opening pages, not a complete coding of every section. It is not a reason to fill the gap with an unrun experiment.

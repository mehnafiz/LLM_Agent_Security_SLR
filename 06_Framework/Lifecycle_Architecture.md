# Lifecycle

Read `Framework_Design.md` first. This file specifies the agent path that is measured, the evaluation stages that measure it, the components of that record, and how a harness would have to log it. The field list, the detector pairs, and the metric denominators are in `Evaluation_Protocol.md`. This file does not add a field that protocol omits.

The harness described below is not in this repository. Building one would not by itself show that a control works. A result would still have to pass G1–G4. No such result is stored here.

## Agent path

The path in Figure 2 is the system under test, not the G1–G4 evaluation checkpoints. A box is included only where the threat model has a surface. Planning is included because later tool and memory operations are conditioned on it. The plan text itself is not an oracle.

| Point | What crosses the boundary | Exposure | Control that can bind here | Where the evidence is stored |
|---|---|---|---|---|
| Configuration | Tool descriptions, implementations, and any recorded permission levels | Poisoned manual; unpinned code; a flat registry presented as least privilege | Pin description and implementation. Record permission levels or waive privilege separation | Run manifest: registry version, manual pin and hash, implementation hash when tool code is in scope, permission levels or the statement that one level exists, and any waiver with its reason |
| Instruction intake | The user instruction | An instruction that requests a tool, memory, peer, or actuator effect outside the task. Chat-only jailbreak is out of scope | Allow-list checked at execution, not by refusing to read the instruction | Case header: instruction identifier |
| Planning | The plan, if the agent emits one | A plan rewritten after untrusted content | Plan-to-call consistency is a detect control. It is not a prevent control | Event: plan text, marked non-oracle, with a sequence number |
| Memory | Reads and writes | Poisoned entry; secret later sent; a write that becomes a future instruction | Write policy; provenance on read; quarantine; delete and retest | If memory is registered: event operation, entry identifier, and provenance label. If Stage 1 waives memory, the manifest records the waiver and these events are absent |
| Outbound call after a memory read | Destination, and the asset identifier when the check names one | A stored secret sent after a read | C8 applies the destination constraint of C2 only to an outbound call that is observed after a relevant memory read | Only on the dashed memory branch in Figure 2, and only when that call is observed. A memory read is not an outbound call. C8 does not follow every C7 event. Sequence number after the memory-read event, destination, and asset identifier when required. If memory is waived, C7 and C8 are not applicable and neither event is written. An ordinary tool destination that does not follow a memory read is a tool-execution field, not this node |
| Tool selection | Chosen tool name | Selection driven by a poisoned description | Deny tools outside the task allow-list | Event: selected tool name. The manual hash stays in the manifest |
| Tool execution | Arguments, result, channel class, and whether the effect committed | Indirect injection in the result; exfiltration; hidden effect in code | Argument and destination constraints; commit only after the check; roll back if the tool can roll back | Event: sequence number, name, arguments, result reference, channel/taint class, committed flag. Implementation hash and permission are manifest fields when tool code is in scope; a waiver replaces them when it is not |
| Peer exchange | Message to or from another agent | A message that causes a tool call on the receiver | Bound the tools a peer may cause; drop the message | If a peer is registered: sender, receiver, message identifier, and the receiver's subsequent tool call. If waived, the manifest records that and these events are absent |
| Actuator | A named physical or external effect | An effect the task did not authorize | The same commit check as tool execution, when an actuator is registered | If registered: event identifier, target, action, and committed flag. Otherwise the manifest records actuators as not applicable |
| Commit and recovery | Side effects left after the run | An effect that survives the session | Restore to the clean baseline, or list the irreversible difference | Event: committed flag, `detector_status`, and `detector_outcome`. Stage 9 restore log. Recovery-rerun task success is a separate column |

Untrusted content is not an extra point on the main loop. It is a carrier that enters at memory, tool execution, or a retrieved result. Retrieval poisoning is that carrier. It is not a separate architecture. The channel/taint field on the event is what C1 uses to show that the carrier stayed in the data channel.

Trust boundaries on this path:

- **TB1, instruction and data.** User instructions and untrusted content are different channels. A malicious instruction is an adversary at TB1, not a reason to treat every instruction as trusted.
- **TB2, planner and tool.** The description, the implementation, and the permission are three fields. Presence in the registry authorizes none of them.
- **TB3, agent and memory.** A stored entry is data. It becomes an instruction only if a write policy promotes it.
- **TB4, agent and peer.** A peer message is untrusted content that may also request an action on the receiving agent.
- **TB5, evaluator and model.** Three records stay distinct. The agent's self-report is not evidence. A raw execution trace is not scoring evidence until integrity, completeness, provenance, and timestamp consistency have been checked. Validated scoring evidence is the trace that passed those checks. This boundary does not claim that instrumentation is tamper-proof. TB5 is an evaluation boundary. It is not a network edge.

If the register has no peer, no memory, no actuator, or no distinct permission levels, the missing point is waived at G1. It is not drawn as if it were present. Figure 2 draws memory and the C8 outbound call on one dashed branch, and draws the peer box dashed. C8 is not a step of the solid loop.

## Evaluation stages

Figure 2 records where each observation point is exercised. Figure 1 draws the ten stages and the gate returns. Figure 4 is the C1–C10 map. Figure 5 is the gate decision for each of G1–G4. Figure 6 is the metric table.

| Stage | Inputs | Work | Outputs | Leave only when |
|---:|---|---|---|---|
| 1 Identify | System description | List the model, tools, memory, peers, actuators, data, and which inputs are untrusted. Record permission levels or state that there is one level. Mark whether tool code, training traces, or self-updates are inside the system | Asset register | The register is written |
| 2 Threat model | Register | For each surface, write adversary, goal, and precondition, or a waiver | Surface catalog | G1 passes |
| 3 Requirements | Catalog | Write each forbidden effect and the user task that must still succeed, as one requirement identifier | Requirement list | Every forbidden effect has an observable check |
| 4 Tests | Requirement list | Build one benign case and one attack case for the same user task. Declare the check as a predicate over trace fields. Declare the carrier the real system reads | Test manifest | Every requirement has at least one pair |
| 5 Run | Manifest | Sandbox tools. Store one immutable run manifest for the configuration and one ordered event trace per case, as specified in `Evaluation_Protocol.md`. Log a runner failure instead of inventing a trace | One linked manifest and one trace per scored case, or a runner failure | G2 passes |
| 6 Score | Traces | Apply only the pre-declared checks. Compute TS, AS, UA, and CS. Identify `B`, `A`, and `A_s`. Do not classify detector outcomes in this stage | Score table | G3 passes |
| 7 Detect | Score table and detector fields | Mark each successful attack pre-commit, post-commit, missed (`no_flag`), or not monitored. Apply the same detector to benign cases. Form `A_m` and `B_m`. Compute DC, FN, and FP. A post-commit flag is not a missed detection and is not in the FN numerator. List unmonitored identifiers and counts apart from those rates | Coverage report | Every successful attack has one of those four marks |
| 8 Mitigate | Coverage report | Add named controls, rerun the same pairs, and rerun a pre-declared changed attack set or record a waiver. Recompute CAC with the same monitored-subset rule | Before-and-after table with baseline TS and protected TS | G4 passes |
| 9 Recover | Leftover failures and the clean baseline | Restore memory and reversible tool effects. Rerun failed identifiers and a sample of earlier passes. Report recovery-rerun task success on that rerun set only | Reassessment | State matches the baseline, or the difference is listed. Recovery-rerun TS is not written into the baseline or protected column |
| 10 Report | All prior outputs | Freeze versions, checks, manifests, traces, waivers, the restore log, and the scoring script | Release record | The record is stored. The next agent change returns to Stage 2 |

Stage 7 does not fail because no detector exists. "Not monitored" is an acceptable mark. It is not a false negative and it is not a false-positive rate of zero. Gate G4 then records that the detect class was not implemented. Stages are not skipped in order to omit a number.

## Fail routes

| Gate | Failure returns to | What must not happen |
|---|---|---|
| G1 after Stage 2 | Stage 2 | Tests are not written for a surface that is neither named nor waived |
| G2 after Stage 5 | Stage 5 | A missing tool log is not scored, and a runner failure is not stored as a complete trace |
| G3 after Stage 6 | Stage 4 if the check or the carrier was wrong; Stage 6 if only the arithmetic was wrong | A Stage 6 number that does not cite a trace field and the protocol denominator is not used. G3 does not accept or reject DC, FN, or FP. Those rates are Stage 7 |
| G4 after Stage 8 | Stage 8 | A control without a rerun is not finished, and first-manifest DC or FP is not copied into a waived CAC cell |

Stage 9 does not have a fifth gate. An irreversible effect is a listed residual, not a failed gate and not a successful recovery. Stage 10 always sends the next change of model, tool, memory policy, peer set, or actuator set back to Stage 2.

## Components

These parts are a description of the record. None is implemented in this repository. Gates are checks on the evaluation record. They are not steps on the agent path. Controls are the C1–C10 catalog in `Mitigation_Strategy.md`.

| Component | Input | Operation | Output | Depends on |
|---|---|---|---|---|
| Register | System description | Name or waive each surface, including memory, peer, actuator, and tool code | Stage 1 register | — |
| Surface catalog | Register | Adversary, goal, precondition, or a waiver | Stage 2 catalog | G1. G1 does not require a runtime trace |
| Manifest | Catalog that passed G1 | Paired cases, predicates, and the immutable run/configuration manifest | Stage 4 manifest | G1 |
| Runtime | Manifest, sandbox | Execute the agent | Ordered events | Register |
| Trace | Events | Store the protocol's event fields, or a runner failure. Do not invent a call. A raw trace becomes scoring evidence only after integrity, completeness, provenance, and timestamp checks | Case trace linked to the run manifest | Runtime. Instrumentation is not claimed to be tamper-proof (TB5) |
| Score | Traces and predicates | Apply only pre-declared checks. Compute TS, AS, UA, and CS | Score table | G2, then G3 |
| Detect | Score table and detector fields | Form `A_m` and `B_m`. Compute DC, FN, and FP. Keep the post-commit count out of both numerators | Coverage report | Stage 7. Not a gate |
| Controls | Named C1–C10 | Bind, rerun the same pairs, produce new traces | Before-and-after table: baseline TS and protected TS | G4 |
| Recovery | Leftovers and the clean baseline | Restore and rerun | Match, a listed residual, and recovery-rerun TS on the rerun set | Stage 9, not a gate |
| Release record | All of the above | Freeze versions, manifests, traces, and the script | Stage 10 record | The gates that passed |

Figure 1 draws this record as the ten-stage ring. G1–G4 sit beside the stages they check. They are not steps on the agent path. Stage 10 stores the release record and stops. A later system change re-enters at Stage 2, not Stage 1. Memory is dashed on Figure 2: Stage 1 registers it or waives it. The trace is the evidence bridge from the runtime to evaluation. G1 uses the Stage 2 catalog and does not require a runtime trace.

## Harness guidance

A harness, if one were built, would wrap the tool executor, the memory store, and, if a peer is in the register, the message path. The model's tokens are not the committed flag. The harness, not the model, records whether the environment applied the call.

A minimal loop matches Figure 2:

1. Read the user instruction from the case file.
2. Let the agent plan and name a tool.
3. The harness checks whatever control is bound, then runs or refuses the tool.
4. Return the tool result, including a carrier the case placed there, and record its channel class.
5. Repeat. A tool result can send the agent back to planning.
6. Store the user-visible reply if the case needs covert success.
7. Give every stored event a sequence number. A monotonic timestamp is optional.

Memory reads and writes are logged when memory is in the register. They are not inserted as a mandatory step when Stage 1 waived memory. A memory read is not an outbound call. The C8 outbound observation is logged only when an outbound call is observed after a relevant memory read on that dashed branch. C8 does not follow every C7 event. If memory is waived, C7 and C8 are not applicable. The same absence rule applies to peers and to actuators.

Tools that can send, write, or delete run against a sandbox. The release record states which tools were actually sandboxed. A tool that escapes the sandbox can produce an effect the trace does not contain. That case is a runner problem or an undefined check, not a defense success.

Write the manifest once per configuration and the event fields in order. If the process crashes, write a runner failure and stop. Do not fill a missing tool call from the model's last sentence. Plan text may be stored and must be marked non-oracle. C5 may compare it with a later call. The comparison is a detector outcome. It is not the attack check.

Enforce prevent and respond controls in the harness, not only as a sentence in the system prompt. An allow-list the model is free to ignore is not C2. C1 is a separation between the data channel and the instruction channel. A filter is one implementation, not a required one. C3 and C4 are pins: log the hash and refuse a mismatch when that surface is in scope. If tool code is waived, record the waiver and do not log a pretended hash. C6's respond action either leaves the committed flag false or records an approval of that call. C10's restore is a separate step before the Stage 9 rerun. A restore that is not rerun is not recovery.

Keep the baseline and the protected run on the same manifest, the same predicates, and the same carriers. The protected run adds the named controls and does not also swap the model or the tool list. If those change, return to Stage 2.

Compute TS, AS, UA, CS, DC, FN, FP, LR, and CAC only as `Evaluation_Protocol.md` defines them. Do not add a composite. Do not replace an empty `A_m` or `B_m` with zero or one. Do not treat `not_monitored` as `no_flag`. Do not put a post-commit flag in the FN numerator. Do not copy the first suite's coverage into the changed-attack cell. Report recovery-rerun task success apart from baseline TS and protected TS. Stage 6 computes TS, AS, UA, and CS. Stage 7 computes DC, FN, and FP.

Store the agent version, pins, predicates, waivers, manifests, traces, and the scoring script. A later reader recomputes the table from the traces without asking the model whether it complied.

Do not put G1–G4 on the request path. Do not score a chat-only jailbreak. Do not treat a harness run as a comparison with WASP, InjecAgent, or CaMeL. Those systems keep their own rates.

## Figure 2

**Caption.** Figure 2. The agent under test as a loop. Instruction leads to planning, then tool selection, then tool execution, with C3 on selection and C2 and C4 on execution. C1 is on the tool result, before that result is treated as an instruction. Re-plan returns to planning. Task completion leaves the loop. Configuration carries C3 only. Commit carries C6 and sits off the loop. C10 is the rerun after commit. Memory writes and later reads are C7, on a dashed branch. C8 is a separate outbound-call node on that branch, drawn only for a call that is observed after a relevant read. A read does not create the call, and C8 does not follow every C7 event. If memory is waived, the branch, including C8, is absent. Peer exchange (C9) is a separate dashed box. Gates G1–G4 are not on this path. C5 detects a plan change and does not stop the call.

## Figure 5

The decision diagram for the four gates is Figure 5. The stage table above is the specification of inputs and outputs. Figure 5 uses those ten stage names and the same return targets. The same returns are drawn on the ring in Figure 1. G1 is decided on the Stage 2 catalog and does not require a runtime trace. Stages 3 and 4 follow that pass and are not a second gate. A scored case at G2 needs a complete trace that has passed the integrity, completeness, provenance, and timestamp checks. A runner failure is logged apart. It is not incomplete scoring evidence, not a passing trace, not a defense success, and it is outside every denominator. G3 follows Stage 6 and checks TS, AS, UA, and CS. It returns to Stage 4 when the check or the carrier is wrong, and to Stage 6 when only the arithmetic is wrong. A change of model, tool registry, memory policy, peer set, or actuator set returns to Stage 2, and that return is not the G1 failure. Stage 7 is not part of G3. G4 is decided on the Stage 8 record: class, baseline TS, protected TS, leftover identifiers, and a changed-attack rerun or a waiver. A security failure is a held attack check or a leftover identifier. It is not a gate failure and not a defense success. Stage 9 is not a gate. Its task-success column is the recovery rerun, not baseline TS or protected TS. A waiver is not a pass.

## Figure 6

Figure 6 is the metric sheet. It defines `B`, `A`, `A_s`, `A_m`, and `B_m`. Stage 6 computes TS, AS, UA, and CS. G3 recomputes those four and does not compute DC, FN, or FP. Stage 7 assigns pre-commit, post-commit, missed (`no_flag`), or not monitored, then computes the detection rates. Baseline, protected, changed-attack, and recovery results are separate panels. Recovery-rerun task success is not the baseline or protected column. A runner failure is outside every denominator. The figure does not add a tenth metric.

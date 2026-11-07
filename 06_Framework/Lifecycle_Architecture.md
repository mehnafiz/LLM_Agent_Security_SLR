# Lifecycle

Read `Framework_Design.md` first. This file specifies the agent path that is measured and the evaluation stages that measure it. Gate evidence is specified in `figures/stage_gates.md`.

## Agent path

The path in Figure 2 is the system under test, not a second set of evaluation stages. A box is included only where the threat model has a surface. Planning is included because later tool and memory operations are conditioned on it. The plan text itself is not an oracle.

| Point | What crosses the boundary | Exposure | Control that can bind here | Trace fields |
|---|---|---|---|---|
| Configuration | Tool descriptions, implementations, and any recorded permission levels | Poisoned manual; unpinned code; a flat registry presented as least privilege | Pin description and implementation. Record permission levels or waive privilege separation | Registry version, pin, permission list |
| Instruction intake | The user instruction | An instruction that requests a tool, memory, or peer effect outside the task. Chat-only jailbreak is out of scope | Allow-list checked at execution, not by refusing to read the instruction | Instruction identifier |
| Planning | The plan, if the agent emits one | A plan rewritten after untrusted content | Plan-to-call consistency is a detect control. It is not a prevent control | Plan text, marked non-oracle |
| Memory | Reads and writes | Poisoned entry; secret later sent; a write that becomes a future instruction | Write policy; provenance on read; quarantine; delete and retest | Operation, entry identifier, provenance label |
| Tool selection | Chosen tool name | Selection driven by a poisoned description | Deny tools outside the task allow-list | Tool name |
| Tool execution | Arguments, result, and whether the effect committed | Indirect injection in the result; exfiltration; hidden effect in code | Argument and destination constraints; commit only after the check; roll back if the tool can roll back | Name, arguments, result, committed flag, order |
| Peer exchange | Message to or from another agent | A message that causes a tool call on the receiver | Bound the tools a peer may cause; drop the message | Destination and the receiver’s subsequent tool call |
| Commit and recovery | Side effects left after the run | An effect that survives the session | Restore to the clean baseline, or list the irreversible difference | Restore log |

Untrusted content is not an eighth point. It is a carrier that enters at memory, tool execution, or a retrieved result. Retrieval poisoning is that carrier. It is not a separate architecture.

Trust boundaries on this path:

- **TB1, instruction and data.** User instructions and untrusted content are different channels. A malicious instruction is an adversary at TB1, not a reason to treat every instruction as trusted.
- **TB2, planner and tool.** The description, the implementation, and the permission are three fields. Presence in the registry authorizes none of them.
- **TB3, agent and memory.** A stored entry is data. It becomes an instruction only if a write policy promotes it.
- **TB4, agent and peer.** A peer message is untrusted content that may also request an action on the receiving agent.
- **TB5, evaluator and model.** Scores are computed from the instrumentation trace. The model’s description of its own behavior is not a trace field. TB5 is an evaluation boundary. It is not a network edge.

If the register has no peer, no memory, or no distinct permission levels, the missing point is waived at G1. It is not drawn as if it were present.

## Evaluation stages

Figure 2 records where each observation point is exercised. The stage order is Figure 4.

| Stage | Inputs | Work | Outputs | Leave only when |
|---:|---|---|---|---|
| 1 Identify | System description | List the model, tools, memory, peers, data, and which inputs are untrusted. Record permission levels or state that there is one level. Mark whether tool code, training traces, or self-updates are inside the system | Asset register | The register is written |
| 2 Threat model | Register | For each surface, write adversary, goal, and precondition, or a waiver | Surface catalog | G1 passes |
| 3 Requirements | Catalog | Write each forbidden effect and the user task that must still succeed, as one requirement identifier | Requirement list | Every forbidden effect has an observable check |
| 4 Tests | Requirement list | Build one benign case and one attack case for the same user task. Declare the check as a predicate over trace fields. Declare the carrier the real system reads | Test manifest | Every requirement has at least one pair |
| 5 Run | Manifest | Sandbox tools. Log the fields in the agent-path table. Log a runner failure instead of inventing a trace | One trace per case | G2 passes |
| 6 Score | Traces | Apply only the pre-declared checks. Compute the metrics in `Evaluation_Protocol.md` | Metric table | G3 passes |
| 7 Detect | Metric table and detector flags | Mark each successful attack as flagged before the effect, flagged after it, missed, or not monitored. Apply the same detector to benign cases | Coverage report | Every successful attack has one of those four marks |
| 8 Mitigate | Coverage report | Add named controls, rerun the same pairs, and rerun a pre-declared changed attack set or record a waiver | Before-and-after table | G4 passes |
| 9 Recover | Leftover failures and the clean baseline | Restore memory and reversible tool effects. Rerun failed identifiers and a sample of earlier passes | Reassessment | State matches the baseline, or the difference is listed |
| 10 Report | All prior outputs | Freeze versions, checks, traces, waivers, and the scoring script | Release record | The record is stored. The next agent change returns to Stage 2 |

Stage 7 does not fail because no detector exists. “Not monitored” is an acceptable mark. Gate G4 then records that the detect class was not implemented. Stages are not skipped in order to omit a number.

## Fail routes

| Gate | Failure returns to | What must not happen |
|---|---|---|
| G1 after Stage 2 | Stage 2 | Tests are not written for a surface that is neither named nor waived |
| G2 after Stage 5 | Stage 5 | A missing tool log is not scored |
| G3 after Stage 6 | Stage 4 if the check or the carrier was wrong; Stage 6 if only the arithmetic was wrong | A number that does not cite a trace field is not used |
| G4 after Stage 8 | Stage 8 | A control without a rerun is not finished |

Stage 9 does not have a fifth gate. An irreversible effect is a listed residual, not a failed gate and not a successful recovery. Stage 10 always sends the next change of model, tool, memory policy, or peer set back to Stage 2.

## Figure 2

**Caption.** Figure 2. Security along the agent path. Each observation point shows the exposure and the control class that can bind there. Dashed lines are trust boundaries TB1–TB4. Trace capture is an evaluation action at Stage 5, not an agent component. Gates G1–G4 do not appear on this path; they are specified in Figure 4.

## Figure 4

The decision diagram for the four gates is Figure 4 in `figures/stage_gates.md`. The stage table above is the specification of inputs and outputs. Figure 4 is the specification of pass, fail, and return. The two descriptions use the same stage names and the same return targets.

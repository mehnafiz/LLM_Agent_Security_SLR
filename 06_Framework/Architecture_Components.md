# Architecture components

These are the parts of AgentShield-LCE. None is implemented in this repository. Gates are checks on the evaluation record. They are not steps on the agent path. Controls are the C1–C10 catalog in `Mitigation_Strategy.md`.

## System under test

- **Input.** The agent, its instruction channel, tool registry, memory if any, and peers if any.
- **Operation.** Plan, select tools, execute tools, read results, and optionally read or write memory or message a peer. The loop repeats until the task ends or a step limit is hit.
- **Output.** Tool calls, memory operations, peer messages, and a user-visible reply.
- **Depends on.** The Stage 1 register for which of those surfaces exist.
- **Not this component.** G1–G4. They do not sit in the loop.

## Observable trace

- **Input.** Events from the sandboxed run.
- **Operation.** Store the G2 record in `Evaluation_Protocol.md`. Store a runner failure instead of inventing a call. Mark plan text as a non-oracle.
- **Output.** One record per case, or one runner failure.
- **Depends on.** The runtime, and on instrumentation the attacker does not control (TB5).

## Evaluation lifecycle

- **Input.** The register, the manifest, and the traces.
- **Operation.** Stages 1–10 in `Lifecycle_Architecture.md`. G1 after Stage 2, G2 after Stage 5, G3 after Stage 6, G4 after Stage 8.
- **Output.** A metric table, a coverage mark, a before-and-after control record, a recovery note or a listed residual, and a release record.
- **Depends on.** The trace. A gate does not call the model to ask whether the attack worked.

## Controls

- **Input.** A named subset of C1–C10, each with its class and observation point.
- **Operation.** Bind the control on the runtime, then rerun the same pairs. Stage 9 restores reversible state and reruns failed identifiers plus a sample of earlier passes.
- **Output.** The G4 table: class, covered identifiers, task success on both runs, leftovers, and a changed-attack rerun or a waiver.
- **Depends on.** The baseline traces. Applying a control is not the output.

## Interaction

| Component | Input | Operation | Output | Depends on |
|---|---|---|---|---|
| Register | System description | Name or waive each surface | Stage 1 register | — |
| Surface catalog | Register | Adversary, goal, precondition, or a waiver | Stage 2 catalog | G1 |
| Manifest | Catalog that passed G1 | Paired cases and predicates | Stage 4 manifest | G1 |
| Runtime | Manifest, sandbox | Execute the agent | Events | Register |
| Trace | Events | Store the G2 fields | Record or runner failure | Runtime |
| Score | Traces and predicates | Apply only pre-declared checks | Metric table | G2, then G3 |
| Controls | Named C1–C10 | Bind, rerun the same pairs | Before-and-after table | G4 |
| Recovery | Leftovers and the clean baseline | Restore and rerun | Match, or a listed residual | Stage 9, not a gate |
| Release record | All of the above | Freeze versions, traces, and the script | Stage 10 record | The gates that passed |

Figure 1 is this table as a drawing. The center band is runtime, trace, then G1–G4. Memory is dashed: Stage 1 registers it or waives it. The trace is the evidence bridge from the runtime to evaluation. G1–G4 are evaluation gates. They assess the record produced at each stage. G1 uses the Stage 2 catalog and does not require a runtime trace. The right-hand outputs are the release record, not a second framework.

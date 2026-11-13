# Limitations and assumptions

AgentShield-LCE has not been run. This file lists what the design does not establish.

## Not established

- No attack-success rate, utility delta, detection rate, overhead, or ranking against another framework has been measured here.
- C1–C10 are design controls. Several host published mechanisms. Hosting them does not transfer those papers’ measurements, and it does not make the mechanism a contribution of this lifecycle.
- A detector flag is not evidence that the effect was stopped. A restore that was not rerun is not evidence that the state is clean.
- Passing G1–G4 means the record contains the named evidence. It does not mean the agent is secure, and it does not apply a numerical threshold. No threshold is defined.

## Assumptions that can fail

- The evaluator can sandbox the tools and can log the G2 fields. If not, G2 fails. The run is not reported as an evaluation.
- The attacker does not forge the trace. An attacker who can is outside TB5 and outside this model.
- The benign case and the attack case share the user task. Otherwise utility under attack is undefined.
- A tool that cannot be rolled back can still be tested. Stage 9 then lists an irreversible residual. That list is not a successful recovery.
- A predicate can be too wide and still be applied consistently. G3 sends that case back to Stage 4 when the check was wrong. The protocol does not notice a wide check by itself.

## What is not scored

- A jailbreak that never reaches a tool, a memory store, or a second agent.
- Hidden reasoning with no trace field.
- Host, hypervisor, and network compromise, unless that host is the system under test.
- Training-time or weight backdoors, unless that supply chain is in the register. The condition is motivated by papers such as BadAgent. It does not put the pipeline into every study.
- Peer behavior the instrumentation cannot read. G2 fails if the receiver’s tool call is not logged.
- Server uptime. Availability in this design is the user task.
- A multi-agent observation that is not a tool-trace predicate. It is not added to single-agent attack success.

## Conditional actors

The content injector is in scope when any untrusted carrier exists. The tool publisher is in scope when third-party tools are selected. The peer, the model supplier, and internal evolution are waived when the register does not include them. A waiver is not a pass, and a waived surface is absent from the metric table. Conditional actors are not drawn as present in every study.

## Literature limit

The comparison in `Framework_Design.md` uses local PDFs and, for that revision, their opening pages. A cell marked not reported was not found there. It is not a proof that the paper lacks the capability. Papers without a local PDF were not used. The AgentDojo paper is not in the retrieved set. It is discussed only where a local paper says it used that benchmark.

## What a finished report can still not say

That the agent is secure. That a control will survive an attack that was not in the manifest. That a waived surface was safe. That a drop in attack success, without task success and the leftover identifiers, finishes the control. The report can say what the pre-declared checks did on the stored traces, which identifiers remain, and whether the changed-attack cell is a measurement or a waiver.

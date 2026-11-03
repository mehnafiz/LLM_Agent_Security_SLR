# AgentShield-LCE

AgentShield-LCE is this project's own lifecycle for evaluating and improving the security of an LLM-based agent. It is a design. It has not been run as an experiment.

It is not a new name for AgentDojo, InjecAgent, WASP, OpenAgentSafety, or any other published benchmark. Those systems answer one slice (a test suite, an attack, or a guard). This lifecycle says how those slices are used together, in order, with a pass/fail gate between them.

## The four review questions, and where each one is answered

| Question | Where it is answered | What "done" means |
|----------|----------------------|-------------------|
| Attack | Stages 2 and 4 | Every in-scope surface has a concrete attacker goal and a test |
| Metrics | Stage 6 | Every reported number points at a trace field, not at the model's own sentence |
| Mitigation | Stages 7 and 8 | Every control is prevent, detect, respond, or recover, and the suite is run again |
| Framework | Stages 1–10 and gates G1–G4 | A later reader can see why the run passed or failed |

Mitigation is not a last chapter. A control is accepted only after Stage 6 is repeated on the same tests.

## The ten stages in one view

| Stage | The question this stage answers | You may leave the stage when |
|------:|----------------------------------|------------------------------|
| 1 | What agent, tools, memory, and data are in scope? | The inventory is written down |
| 2 | What can an attacker do on each surface? | Gate G1: tools, memory, and other agents are covered or explicitly waived |
| 3 | Which of those actions are forbidden, and which user tasks must still work? | Each forbidden action has an observable check |
| 4 | What is the paired benign task and attack for each check? | Each requirement has at least one pair |
| 5 | What happened when the suite was run? | Gate G2: every case has a tool-level trace, or a recorded run failure |
| 6 | Did the attack succeed, and did the user task still succeed? | Gate G3: each number cites a trace field |
| 7 | Which successful attacks were visible before the harm? | Each success is marked detected, missed, or not monitored |
| 8 | Which control was added, and what still fails? | Gate G4: class, covered checks, task-success change, and leftovers are recorded |
| 9 | Is the agent clean again, and do old passes still pass? | State matches the clean baseline, or the difference is listed |
| 10 | Can someone else replay the gate decisions? | The release record is stored. The next change returns to Stage 2 |

Details of inputs, outputs, and fail routes are in `Lifecycle_Architecture.md`. Surfaces are in `Threat_Model.md`. Scores are in `Evaluation_Protocol.md`. Controls are in `Mitigation_Strategy.md`. Gates are in `figures/stage_gates.md`.

## What this document does not say

It does not assign a journal quartile. It does not copy an attack-success rate from a paper as if this project re-ran that paper. An arXiv PDF in the corpus is not treated as the published version.

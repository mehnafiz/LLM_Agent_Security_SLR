# Figure captions

No PDF figures were produced. Each SVG is the editable source. Each PNG is a render of that SVG. The master sheet nests the same six drawings. It does not add a rule.

Abbreviations used on the figures: G1–G4 are the evaluation checkpoints. C1–C10 are the controls in `Mitigation_Strategy.md`. TB1–TB5 are the trust boundaries in `Threat_Model.md`. TS, AS, UA, CS, DC, FN, FP, LR, and CAC are the metrics in `Evaluation_Protocol.md`. A waiver is not a pass.

Color: navy title bars; blue for the runtime; purple for evaluation; red for threats and failure returns; green for controls and the release record; orange for inputs and configuration; grey for the trace.

## Figure 1

File: `figures/Figure_01_Overall_Framework.svg`

**Caption.** AgentShield-LCE at a glance. Inputs enter the agent runtime. Memory is drawn dashed because Stage 1 either registers it or waives it. The trace is the evidence bridge from runtime to evaluation. G1–G4 are evaluation gates, not runtime steps. They assess the record produced at each stage. G1 uses the threat model and the surface register and does not require a runtime trace. Outputs are the release record. A control is a new execution, not an arrow from a gate into the loop.

**Placement.** Opening of the framework section.

## Figure 2

File: `figures/Figure_02_Agent_Loop.svg`

**Caption.** The agent loop, with the attack surfaces and C1–C10 beside it. Instruction leads to planning (C5), then selection (C3) and execution (C2 and C4), then the tool result (C1). Re-plan returns to planning. Task completion leaves the loop. Configuration carries C3 only. C4 is on execution, not on that box. C6 is the commit boundary. C10 is the later rerun. Memory (C7) and peer exchange (C9) are dashed and appear only when Stage 1 registers them. C8 is the outbound call after a memory read. Tool implementation is a surface. A waiver of tool code is a scope decision, not a surface. C5 does not stop the call. Gates are not on this figure. TB5 is not drawn, because it is not a network edge.

**Placement.** With `Lifecycle_Architecture.md`.

## Figure 3

File: `figures/Figure_03_Threat_Model.svg`

**Caption.** Actors, assets, trust boundaries, and surfaces. The user instruction enters the agent. The agent sits in the center, with a separate link to tools, a dashed link to memory, and a dashed link to a peer. Those links are not a sequence from tools through memory to the peer. Memory and peer appear only when Stage 1 registers them. Dashed actors stay conditional. TB1 keeps instruction and untrusted data in separate channels, and a direct instruction still faces the task allow-list. TB5 is the evaluator and the trace. It is not a network edge. The surface is labeled tool implementation. A waiver of tool code is a scope note, not a surface. An attempt is not the scored effect.

**Placement.** With `Threat_Model.md`.

## Figure 4

File: `figures/Figure_04_Stage_Gates.svg`

**Caption.** G1 after Stage 2, G2 after Stage 5, G3 after Stage 6, G4 after Stage 8. The stage strip uses the ten names in `Lifecycle_Architecture.md`. A scored case needs a complete trace. A runner failure is logged apart. It is not a passing trace, not a defense success, and it stays out of every denominator. G3 returns to Stage 4 when the check or the carrier is wrong, and to Stage 6 when only the arithmetic is wrong. The other fails return to Stage 2, Stage 5, or Stage 8. The diamond asks whether the gate-specific criteria are met. Stage 7 does not fail when the detector mark is “not monitored.” Stage 9 and Stage 10 are not gates. A waiver is not a pass. No gate declares the agent secure.

**Placement.** With `Evaluation_Protocol.md`.

## Figure 5

File: `figures/Figure_05_Control_Map.svg`

**Caption.** C1–C10 from threat to point, class, evidence, and metric. Green is prevent. Purple is detect only. Orange includes a response after a flag. Blue is recover. C4’s evidence cell has two conditions. If tool code is in scope, the implementation hash and permission are logged. If it is waived, the scope register records the waiver. That waiver is not a verification of the implementation. C10 lists LR, the leftover set from mitigation, and TS from the recovery rerun, as two measurements. DC is undefined when A_s is empty or no detector ran. FN is undefined when A_s is empty. FP is undefined when no detector ran. “Not monitored” is not a false-positive rate of zero. CAC is the changed-attack cell at G4, or a waiver, and is not a row of this map. No row has been measured here.

**Placement.** With `Mitigation_Strategy.md`.

## Figure 6

File: `figures/Figure_06_Evaluation_Workflow.svg`

**Caption.** Stages 1–10 as a researcher would run them. The Stage 5 box says a scored case needs a trace, a runner failure is not a trace, and that failure is excluded from metric denominators. Stage 9, recovery, and Stage 10, the release record, are drawn as two boxes. Neither is a gate. The baseline and the protected run use the same manifest. The protected run adds named controls and new traces. A changed-attack manifest is declared before the rerun, or the cell states a waiver. Recovery restores reversible state and reruns failed identifiers and a sample of earlier passes. Irreversible effects stay listed. A lower AS alone does not finish mitigation. A runner failure is not a defense success.

**Placement.** End of the method, before the limitations.

## Master infographic

File: `figures/Master_Framework.svg`

**Caption.** Figures 1–6 composed from the six SVG sources, in that order. The master is not a scaled copy of the PNG files. It uses the same drawings and the same rules: the trace is the evidence bridge from runtime to evaluation, G1 does not require a runtime trace, C1–C10 sit at the points in Figure 2, a runner failure is excluded from metric denominators, and the metrics are TS, AS, UA, CS, DC, FN, FP, LR, and CAC. The sheet adds no rule and reports no measurement.

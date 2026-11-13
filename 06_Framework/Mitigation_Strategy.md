# Mitigation

A control counts only when it has a class, an observation point, a mechanism, a protected property, a rerun on the same pairs, and a leftover list. Publishing a detector without a prevent, respond, or recover action is a detect result. It is not a claim that the effect was stopped.

The mechanisms below are design controls. Several of them host techniques already reported in the retrieved PDFs. Hosting a technique does not transfer that paper’s measurements to this lifecycle, and it does not make the technique a contribution of AgentShield-LCE.

## Classes

| Class | When it acts | Fair claim | Rerun required |
|---|---|---|---|
| Prevent | Before the effect commits | The forbidden effect did not occur | The full paired suite |
| Detect | During the run, at a named boundary | The case was flagged, and whether the flag preceded the commit | Successful attacks and the benign cases, using the same detector |
| Respond | After a flag | The effect was blocked, or a person approved that call | The same cases, plus the change in task success |
| Recover | After the effect or a suspected poison | State matches the clean baseline, or the irreversible difference is listed | Failed identifiers and a sample of earlier passes |

Prevent stops the effect. Detect notices it. Respond acts on a notice. Recover cleans state. A confirmation prompt is a respond control. It does not replace an allow-list, because an unattended agent cannot wait on a person.

## Control catalog

Figure 5 draws each control from the threat to the metric. The full mechanism stays in the table below. The limitation of each control is part of the row, not an afterword. No row is a measured reduction.

| ID | Threat | Point | Class | Mechanism | Evidence and check | Metric | Limitation |
|---|---|---|---|---|---|---|---|
| C1 | Indirect prompt injection from untrusted content | Tool execution, before the result is treated as an instruction | Prevent | Keep the tool result, page, email, or retrieved passage in a data channel. Do not concatenate it into the instruction channel. A filter that deletes instruction-shaped spans is one implementation, not a required component | The trace shows the result in the data channel. The Stage 4 attack check is false, or the benign check fails and is reported | Attack success; utility under attack | An adaptive injection can avoid a filter pattern. Benign instructions the task needed can be removed. Either failure stays in the leftover list. Adapted from published filters. Not measured here |
| C2 | Unauthorized tool use, including instruction-channel abuse and exfiltration | Tool execution, before commit | Prevent | Allow only tool names declared for that requirement. Constrain arguments and outbound destinations to predicates declared in Stage 4 | The committed tool name, arguments, and destination satisfy the Stage 4 predicate | Attack success on that predicate | A wide predicate accepts an attacker-chosen argument that still matches. G3 then returns the case to Stage 4. Design control. Not measured here |
| C3 | Tool-description poisoning | Configuration and tool selection | Prevent | Call a tool only when its description hash matches the pin in the register | The registry version and pin are in the trace, and the selected tool name matches the pinned manual | Attack success on the tool-name check | A pin does not make a malicious tool benign. It freezes the manual the evaluator chose to trust. Design control. Not measured here |
| C4 | Tool-code backdoor or an effect the description does not show | Tool execution | Prevent | Call the implementation only when its hash and permission match the pin. Deny the call if tool code is in scope and unpinned | If tool code is in scope, the implementation hash and permission are logged and the declared effect is absent. If Stage 1 waives tool code, the scope register records that waiver. The waiver is not evidence that the implementation was verified | Attack success on the effect | Out of scope when Stage 1 waives tool code. A matching hash can still be a tool the user should not have trusted. Design control. Not measured here |
| C5 | Indirect injection that changes the plan after untrusted data | Planning, compared with the later call | Detect | If a plan was emitted before the untrusted read, flag a later tool call that the plan did not contain | The detector flag is before or after commit, and the plan text is marked non-oracle | Detection coverage. Undefined when no attack succeeds | A plan written after the poison can match the attacker’s goal and will not be flagged. This control does not prevent the call. Adapted from plan-consistency defenses. Not measured here |
| C6 | A committed effect that should have been stopped | Tool execution, at commit | Detect and respond | Flag the call at the commit boundary. Respond by not committing, or by asking for approval of that call | The detector flag and the committed flag are both present. A response that blocks the call leaves the committed flag false | Detection coverage; attack success; task success | A fixed flag misses attacks outside the patterns it encodes. G4 requires a changed-attack rerun or a waiver. Approval of every call is not an allow-list. Design control. Not measured here |
| C7 | Memory poisoning | Memory write and later read | Prevent and detect | Accept a write only from carriers the write policy names. On read, check the stored provenance label and quarantine a label that does not match | The memory operation, entry identifier, and provenance label are in the trace | Attack success on the later read | Provenance shows origin. It does not show that the text is harmless. Design control. Not measured here |
| C8 | Memory disclosure | Memory read followed by an outbound call | Prevent | The destination constraint of C2 applies to data read from memory | The outbound destination is in the trace and fails the attack check | Attack success on the destination | A permitted tool can still leak data if the destination predicate is broader than the task. Design control. Not measured here |
| C9 | Peer-caused tool use | Peer exchange | Prevent, detect, and respond | A peer message may name only tools in the peer allow-list. A message that would cause any other tool is flagged and dropped | The receiver’s subsequent tool call is logged. The score is kept separate from single-agent attack success | Attack success on that call, reported separately | This does not verify an agent-to-agent protocol implementation. Design control. Not measured here |
| C10 | Poisoned memory or a reversible tool effect | After commit | Recover | Quarantine or delete the entry, roll back a reversible tool effect, restore the clean baseline, and rerun the failed identifiers plus a sample of earlier passes | The restore log and the rerun traces match the clean baseline, or the difference is listed | Leftover identifiers; task success on the rerun | Irreversible effects remain residuals. A restore that is not rerun is not recovery. Design control. Not measured here |

C1 is the class of instruction and data separation. Published filters are examples of an implementation. C5 is the class of plan-to-call consistency. C3 and C4 are pins, not a general supply-chain audit. C6 is the class of commit-time monitoring. None of these identifiers denotes a new algorithm.

## Properties

The property names are used only as follows.

- **Confidentiality.** User data or memory content is not sent to a destination outside the predicate for that requirement.
- **Integrity.** The tool effect and the memory state match the user task and the pinned tool.
- **Authorization.** The tool name, arguments, and any peer-caused call stay inside the allow-list for that requirement.
- **Availability.** The benign check still holds. This is the user task, not server uptime.

## Changed attacks

Stage 8 is not finished when attack success falls on the original manifest. The record lists:

- requirement identifiers that still fail;
- task success on the baseline run and on the protected run;
- which of the four classes was not implemented;
- either coverage and false positives on a second attack manifest declared before the rerun, or a waiver that states why the original distribution is the only one in scope.

The second manifest exists because disclosed defenses and fixed monitors have failed when the attack pattern changed. Those are findings of the papers that ran the tests. This lifecycle requires the rerun or the waiver. It does not claim that the rerun restores coverage.

## What is not in this file

This file does not rank published defenses. It does not assign a residual-risk score. A control is literature-established only when `Framework_Design.md` names a local PDF that describes that mechanism. The other controls are design adaptations. None has been run in this project.

## Figure 5

**Caption.** Figure 5. One row for each of C1–C10. The row runs from the threat to the runtime point, the class, the trace evidence, and the metric. C4 splits the evidence cell: a logged hash and permission when tool code is in scope, and a scope-register waiver when it is not. The waiver is not a verification. C10’s metric cell names LR, the leftover set, and TS on the recovery rerun as two measurements. DC is undefined when A_s is empty or no detector ran. FN is undefined when A_s is empty. FP is undefined when no detector ran. “Not monitored” is not drawn as a false-positive rate of zero. CAC stays in the footer as the G4 cell or a waiver. G3 cites the evidence. The full mechanism of each control stays in the table above. Detect is not drawn as prevent. No row is a measured reduction.

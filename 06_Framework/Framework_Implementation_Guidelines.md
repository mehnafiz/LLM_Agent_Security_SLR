# Implementation guidelines

AgentShield-LCE is a harness around a tool-using agent. The harness is not in this repository. Building it would not by itself show that a control works. A result still has to pass G1–G4.

## What to wrap

Wrap the tool executor, the memory store, and, if a peer is in the register, the message path. The model’s tokens are not the committed flag. The harness, not the model, records whether the environment applied the call.

A minimal loop matches Figure 2:

1. Read the user instruction from the case file.
2. Let the agent plan and name a tool.
3. The harness checks whatever control is bound, then runs or refuses the tool.
4. Return the tool result, including a carrier the case placed there.
5. Repeat. A tool result can send the agent back to planning.
6. Store the user-visible reply if the case needs covert success.

Memory reads and writes are logged when memory is in the register. They are not inserted as a mandatory step when Stage 1 waived memory. The same rule applies to peers.

## Sandbox

Tools that can send, write, or delete run against a sandbox. The release record states which tools were actually sandboxed. A tool that escapes the sandbox can produce an effect the trace does not contain. That case is a runner problem or an undefined check, not a defense success.

## Trace

Write the G2 fields in `Evaluation_Protocol.md`, in order. If the process crashes, write a runner failure and stop. Do not fill a missing tool call from the model’s last sentence.

Plan text may be stored and must be marked non-oracle. C5 may compare it with a later call. The comparison is a detector flag. It is not the attack check.

## Controls

Enforce prevent and respond controls in the harness, not only as a sentence in the system prompt. An allow-list the model is free to ignore is not C2. C1 is a separation between the data channel and the instruction channel. A filter is one implementation, not a required one. C3 and C4 are pins: log the hash and refuse a mismatch when that surface is in scope. If tool code is waived, do not log a pretended hash.

C6’s respond action either leaves the committed flag false or records an approval of that call. C10’s restore is a separate step before the Stage 9 rerun. A restore that is not rerun is not recovery.

## Evaluation

Keep the baseline and the protected run on the same manifest, the same predicates, and the same carriers. The protected run adds the named controls and does not also swap the model or the tool list. If those change, return to Stage 2.

Compute TS, AS, UA, CS, DC, FN, FP, LR, and CAC only as `Evaluation_Protocol.md` defines them. Do not add a composite. Do not replace an empty success set with zero or one. Do not copy the first suite’s coverage into the changed-attack cell.

Store the agent version, pins, predicates, waivers, traces, and the scoring script. A later reader recomputes the table from the traces without asking the model whether it complied.

## What not to build

Do not put G1–G4 on the request path. Do not score a chat-only jailbreak. Do not treat the first successful harness run as a comparison with WASP, InjecAgent, or CaMeL. Those systems keep their own rates.

# Mitigation

This is the priority part of the review. A defense counts only when it has a class, a place in the lifecycle, a rerun, and a leftover list.

## Four classes

| Class | When it acts | A fair claim | Required rerun |
|-------|--------------|--------------|----------------|
| Prevent | Before the effect. Examples: tool allow-list, argument limits, separating untrusted text from instructions, pinning a tool description. | The forbidden effect did not happen | The full paired suite |
| Detect | While the run is in progress. Examples: a check at tool return, or on memory read. | The case was flagged, and at what moment | Successful attacks and benign cases |
| Respond | After a flag. Examples: block the call, ask a person, drop a peer message. | The effect stopped, or a person approved it | The same cases, plus the change in task success |
| Recover | After the effect or a suspected poison. Examples: roll back a tool side effect, quarantine a memory entry. | State matches the clean baseline | The failed IDs and a sample of earlier passes |

Prevent stops the effect. Detect only notices it. Respond acts on a notice. Recover cleans up. A paper that only detects an injection has not shown prevention.

## Which class sits on which surface

| Surface | Prevent | Detect | Respond | Recover |
|---------|---------|--------|---------|---------|
| Tool result or page | Keep untrusted text out of the instruction channel | Watch the tool-return boundary | Block the call or ask for confirmation | Replay the user task from clean context |
| Tool description | Accept only pinned descriptions | Compare the call with the user goal | Deny the tool | Remove it from the registry |
| Memory | Decide what may be written | Check provenance on read | Quarantine the entry | Delete or repair, then reassess |
| Other agents | Limit what a peer may cause | Cross-check a message that would call a tool | Drop the message | Rerun the joint task |
| Tool code | Pin the implementation and its permissions | Watch the effect | Stop the tool | Roll back side effects |

## Leftover risk

Stage 8 is not finished when the attack-success number falls. The record must list:

- requirement IDs that still fail;
- how task success changed;
- which of the four classes was not implemented.

Asking a person to approve every call is a respond control. It does not replace an allow-list, because an unattended agent cannot wait.

## What is not in this file

This file does not rank published defenses with a score this project did not compute. Per-paper notes belong in `05_LITERATURE_ANALYSIS/Paper_Analysis_Matrix.xlsx`, and only in rows whose text was actually read.

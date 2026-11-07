#!/usr/bin/env python3
"""Editable source for AgentShield-LCE Figures 1–6.

Renders SVG files beside this script. PNG export is a separate step
(headless Chrome). Terminology matches the framework documents.
"""

from pathlib import Path
import html
import math

OUT = Path(__file__).resolve().parent

INK = "#1C2833"
MUTED = "#5D6D7E"
BLUE_F, BLUE_S = "#EAF2F8", "#1A5276"
RED_F, RED_S = "#FDEDEC", "#922B21"
ORANGE_F, ORANGE_S = "#FEF5E7", "#B9770E"
GREEN_F, GREEN_S = "#E8F8F5", "#196F3D"
GREY_F, GREY_S = "#F4F6F7", "#5D6D7E"
LINE = "#1C2833"
WHITE = "#FFFFFF"


def esc(text):
    return html.escape(str(text), quote=True)


class Svg:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.p = []

    def add(self, s):
        self.p.append(s)

    def rect(self, x, y, w, h, fill, stroke, rx=8, sw=1.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )

    def poly(self, points, fill, stroke, sw=1.6):
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        self.add(
            f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=1.6, marker="arr", dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" fill="none"{d}{m}/>'
        )

    def path(self, d, stroke=LINE, sw=1.6, marker="arr", dash=None, fill="none"):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}{m}/>'
        )

    def text(self, x, y, lines, size=14, weight=400, fill=INK, anchor="start", lh=None):
        if isinstance(lines, str):
            lines = [lines]
        lh = lh or (size + 3)
        tw = ' font-weight="600"' if weight >= 600 else ""
        spans = []
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else lh
            spans.append(f'<tspan x="{x:.1f}" dy="{dy}">{esc(line)}</tspan>')
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{tw}>{"".join(spans)}</text>'
        )

    def center_in(self, x, y, w, h, lines, size=13, weight=400, fill=INK, lh=None):
        if isinstance(lines, str):
            lines = [lines]
        lh = lh or (size + 3)
        block = lh * len(lines)
        ty = y + (h - block) / 2 + size - 1
        self.text(x + w / 2, ty, lines, size=size, weight=weight, fill=fill, anchor="middle", lh=lh)

    def save(self, name):
        marker = """
        <defs>
          <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#1C2833"/>
          </marker>
          <marker id="arrRed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#922B21"/>
          </marker>
          <marker id="arrGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#196F3D"/>
          </marker>
          <marker id="arrOrange" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#B9770E"/>
          </marker>
          <marker id="arrBlue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#1A5276"/>
          </marker>
        </defs>
        """
        body = "\n".join(self.p)
        doc = (
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}">\n'
            f'<rect width="100%" height="100%" fill="{WHITE}"/>\n'
            f'<style>text {{ font-family: Helvetica, Arial, sans-serif; }}</style>\n'
            f"{marker}\n{body}\n</svg>\n"
        )
        path = OUT / name
        path.write_text(doc, encoding="utf-8")
        return path


def legend(s, x, y):
    items = [
        (BLUE_F, BLUE_S, "Agent path"),
        (RED_F, RED_S, "Threat or attack carrier"),
        (ORANGE_F, ORANGE_S, "Evaluation gate"),
        (GREEN_F, GREEN_S, "Control"),
        (GREY_F, GREY_S, "External or record"),
    ]
    cx = x
    for fill, stroke, label in items:
        s.rect(cx, y, 16, 16, fill, stroke, rx=3, sw=1.4)
        s.text(cx + 22, y + 13, label, size=12, fill=INK)
        cx += 22 + 8 * len(label) + 28


def figure_1():
    """Master view: the evaluation ring is closed. Stage 10 returns to Stage 2."""
    W, H = 1800, 1760
    s = Svg(W, H)
    s.text(48, 38, "Figure 1. AgentShield-LCE, the closed evaluation cycle", size=22, weight=700)
    s.text(
        48,
        64,
        "Clockwise on the ring is a pass. Stage 10 returns to Stage 2. Stage 1 enters once and is not repeated.",
        size=14,
        fill=MUTED,
    )
    legend(s, 48, 84)

    cx, cy, R = 900, 980, 560
    bw, bh = 188, 74
    nodes = [
        ("S2", ["Catalog surfaces", "or waive them"], "stage"),
        ("G1", ["Fail returns to S2", "Do not write tests"], "gate"),
        ("S3–S4", ["Pair the task and", "declare the checks"], "stage"),
        ("S5", ["Sandbox run.", "Keep the tool trace"], "stage"),
        ("G2", ["Fail returns to S5", "Do not score a gap"], "gate"),
        ("S6", ["Score only the", "declared trace check"], "stage"),
        ("G3", ["Wrong check → S4", "Bad arithmetic → S6"], "gate"),
        ("S7–S8", ["Coverage, then", "controls and rerun"], "stage"),
        ("G4", ["Fail returns to S8", "Rerun or waiver"], "gate"),
        ("S9", ["Restore, or list", "what cannot be undone"], "stage"),
        ("S10", ["Freeze the record.", "Then return to S2"], "stage"),
    ]
    n = len(nodes)

    def polar(theta, radius):
        return cx + radius * math.sin(theta), cy - radius * math.cos(theta)

    s.add(
        f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#D4E6F1" stroke-width="14"/>'
    )
    s.add(
        f'<circle cx="{cx}" cy="{cy}" r="268" fill="#F8FBFD" stroke="{BLUE_S}" stroke-width="1.6"/>'
    )

    centers = []
    for i, (code, lines, kind) in enumerate(nodes):
        theta = i * 2 * math.pi / n
        x, y = polar(theta, R)
        centers.append((x, y, theta))
        fill, stroke = (ORANGE_F, ORANGE_S) if kind == "gate" else (BLUE_F, BLUE_S)
        s.rect(x - bw / 2, y - bh / 2, bw, bh, fill, stroke)
        s.center_in(x - bw / 2, y - bh / 2, bw, bh, [code] + lines, size=13, weight=700, lh=17)

    for i in range(n):
        theta = (i + 0.5) * 2 * math.pi / n
        x1, y1 = polar(theta - 0.11, R)
        x2, y2 = polar(theta + 0.05, R)
        closing = i == n - 1
        color = ORANGE_S if closing else BLUE_S
        marker = "arrOrange" if closing else "arrBlue"
        s.line(x1, y1, x2, y2, stroke=color, marker=marker, sw=2.4 if closing else 1.8)
        if closing:
            lx, ly = polar(theta, R + 78)
            s.text(lx, ly, ["Next change"], size=13, weight=700, fill=ORANGE_S, anchor="middle")

    # Stage 1 is the entry, outside the repeating ring.
    s2x, s2y, _ = centers[0]
    s.rect(s2x - 150, 168, 300, 70, BLUE_F, BLUE_S)
    s.center_in(s2x - 150, 168, 300, 70, ["S1  Identify the agent", "Entry only. Not repeated."], size=14, weight=700, lh=18)
    s.line(s2x, 238, s2x, s2y - bh / 2 - 2, stroke=BLUE_S, marker="arrBlue", sw=1.8)
    s.text(s2x + 16, 268, "enters the cycle", size=12, fill=BLUE_S)

    # Center: the object the cycle measures.
    s.text(cx, cy - 168, "System under test", size=16, weight=700, fill=BLUE_S, anchor="middle")
    s.text(cx, cy - 142, "Measured by S5. Rerun by S8.", size=13, fill=MUTED, anchor="middle")
    steps = [
        (cx - 230, cy - 118, "Configuration"),
        (cx - 70, cy - 118, "Instruction"),
        (cx + 90, cy - 118, "Planner"),
        (cx - 230, cy - 70, "Memory"),
        (cx - 70, cy - 70, "Tool selection"),
        (cx + 90, cy - 70, "Tool execution"),
        (cx - 150, cy - 22, "Peer, if present"),
        (cx + 10, cy - 22, "Effect commit"),
    ]
    for x, y, label in steps:
        s.rect(x, y, 140, 36, BLUE_F, BLUE_S, rx=6)
        s.center_in(x, y, 140, 36, label, size=12, weight=600)
    s.text(cx, cy + 36, "Untrusted content enters memory and tool execution.", size=12, weight=600, fill=RED_S, anchor="middle")
    s.text(cx, cy + 62, "Controls, accepted only after G4", size=13, weight=700, fill=GREEN_S, anchor="middle")
    controls = [("Prevent", cx - 230), ("Detect", cx - 112), ("Respond", cx + 6), ("Recover", cx + 124)]
    for label, x in controls:
        s.rect(x, cy + 76, 100, 34, GREEN_F, GREEN_S, rx=6)
        s.center_in(x, cy + 76, 100, 34, label, size=13, weight=700)
    s.text(cx, cy + 136, "A gate checks the record. It is not on the serving path.", size=12, fill=INK, anchor="middle")
    s.text(cx, cy + 158, "TB5: the score uses the trace, not the model’s sentence.", size=12, fill=INK, anchor="middle")

    s.text(
        48,
        1708,
        "A fail named on a gate steps back inside the ring. It does not start a new lifecycle. Figures 2–6 give the path, the threat map, the gate evidence, the controls, and the metrics.",
        size=13,
        fill=MUTED,
    )
    s.save("Figure_01_Overall_Framework_Architecture.svg")


def figure_2():
    W, H = 1760, 1040
    s = Svg(W, H)
    s.text(36, 36, "Figure 2. Security along the agent path", size=20, weight=700)
    s.text(
        36,
        60,
        "Observation points of the system under test. This is not the evaluation-stage sequence. Gates are in Figure 4.",
        size=13,
        fill=MUTED,
    )
    legend(s, 36, 78)

    points = [
        ("Configuration", "TB2", "Poisoned manual;", "unpinned code", "Pin description", "and implementation"),
        ("Instruction", "TB1", "Unauthorized tool", "request on this channel", "Allow-list is applied", "at execution, not here"),
        ("Planning", "—", "Plan rewritten after", "untrusted content", "Detect: plan-to-call", "consistency (C5)"),
        ("Memory", "TB3", "Poisoned entry;", "later disclosure", "Write policy;", "provenance on read"),
        ("Tool selection", "TB2", "Wrong tool chosen", "from the manual", "Deny names outside", "the task allow-list"),
        ("Tool execution", "TB1, TB2", "Injected result;", "bad arguments", "Data channel; argument", "and destination limits"),
        ("Peer exchange", "TB4", "Message causes a", "tool call", "Peer allow-list;", "else drop the message"),
        ("Commit / recover", "—", "Effect survives", "the session", "Block commit; roll back", "or list irreversible"),
    ]
    x0, y0 = 36, 140
    cw, ch, gap = 200, 430, 16
    for i, (name, tb, e1, e2, c1, c2) in enumerate(points):
        x = x0 + i * (cw + gap)
        s.rect(x, y0, cw, ch, WHITE, "#D5D8DC", rx=10, sw=1.2)
        s.rect(x + 10, y0 + 14, cw - 20, 64, BLUE_F, BLUE_S)
        s.center_in(x + 10, y0 + 14, cw - 20, 64, [f"{i+1}  {name}", tb], size=13, weight=700, lh=18)
        s.rect(x + 10, y0 + 96, cw - 20, 130, RED_F, RED_S)
        s.text(x + 22, y0 + 120, "Exposure", size=12, weight=700, fill=RED_S)
        s.text(x + 22, y0 + 146, [e1, e2], size=13, lh=18)
        s.rect(x + 10, y0 + 242, cw - 20, 130, GREEN_F, GREEN_S)
        s.text(x + 22, y0 + 266, "Control", size=12, weight=700, fill=GREEN_S)
        s.text(x + 22, y0 + 292, [c1, c2], size=13, lh=18)
        if i < len(points) - 1:
            s.line(x + cw, y0 + 46, x + cw + gap, y0 + 46, stroke=BLUE_S, marker="arrBlue", sw=1.6)
    s.text(36, 600, "The arrows are the usual pass. Memory may be read again after a tool result. A missing peer, memory, or permission split is waived at G1.", size=13, fill=INK)

    s.rect(36, 640, 1688, 150, RED_F, RED_S, rx=10)
    s.text(52, 670, "Attack carriers entering the path", size=15, weight=700, fill=RED_S)
    s.text(52, 700, "Untrusted content (page, email, retrieval, tool result) enters at memory and at tool execution. It is not an eighth observation point.", size=14)
    s.text(52, 726, "A poisoned tool description enters at configuration and is observed at tool selection. Tool code is observed at execution.", size=14)
    s.text(52, 752, "A peer message enters at peer exchange. A malicious instruction enters at instruction intake and is judged by the later tool check.", size=14)

    s.rect(36, 810, 1688, 180, GREY_F, GREY_S, rx=10)
    s.text(52, 842, "What Stage 5 records at these points", size=15, weight=700)
    s.text(52, 872, "Registry version and pin; instruction identifier; plan text marked non-oracle; memory operation, entry identifier, and provenance;", size=14)
    s.text(52, 896, "tool name, arguments, result, committed flag, and order; peer destination and the receiver’s subsequent tool call; restore log.", size=14)
    s.text(52, 928, "TB5. The score is computed from those fields. The model’s statement that it refused or complied is not a field.", size=14, weight=600)
    s.text(52, 958, "Chat-only jailbreak, with no tool, memory, or peer effect, has no check on this path and is out of scope.", size=14)
    s.save("Figure_02_Agent_Lifecycle_Security.svg")


def figure_3():
    W, H = 1760, 980
    s = Svg(W, H)
    s.text(36, 36, "Figure 3. Threat-model map", size=20, weight=700)
    s.text(
        36,
        60,
        "One row is one actor. Dashed rows are waived unless Stage 1 puts that input inside the system under test.",
        size=13,
        fill=MUTED,
    )
    legend(s, 36, 78)

    headers = [
        (36, 250, "Actor"),
        (300, 230, "Can"),
        (544, 250, "Boundary"),
        (808, 230, "Surface"),
        (1072, 280, "Asset harmed"),
        (1366, 330, "Scored objective"),
    ]
    s.rect(36, 120, 1688, 36, GREY_F, GREY_S, rx=6)
    for x, w, label in headers:
        s.text(x + 12, 144, label, size=13, weight=700)

    rows = [
        (False, "Content injector", "Write text the agent will read", "TB1", "Untrusted content", "Task, data, tool effect", "Replacement, exfiltration, unauthorized call"),
        (False, "Instruction adversary", "Supply the user instruction", "TB1", "Instruction channel", "Tool effect, user data", "Unauthorized tool effect only"),
        (False, "Tool publisher", "Publish a manual or implementation", "TB2", "Description or code", "Tool effect, user data", "Wrong tool, or a hidden effect"),
        (False, "Peer agent", "Send a message", "TB4", "Peer message", "Tool effect on receiver", "Peer-caused call, scored alone"),
        (True, "Model or trace supplier", "Poison weights or tool-use traces", "Supply chain", "Model or tool code", "Tool effect", "Only if that pipeline is listed"),
        (True, "Internal evolution", "Write a later session’s state", "TB3", "Memory or registry", "Memory, user task", "Only if the agent self-updates"),
    ]
    y = 170
    rh = 100
    for dashed, actor, can, boundary, surface, asset, objective in rows:
        dash = "7 4" if dashed else None
        fill = "#FDEDEC" if not dashed else "#FBFCFC"
        stroke = RED_S if not dashed else GREY_S
        s.rect(36, y, 1688, rh - 8, fill, stroke, rx=8, dash=dash, sw=1.4)
        vals = [
            (36, 250, actor),
            (300, 230, can),
            (544, 250, boundary),
            (808, 230, surface),
            (1072, 280, asset),
            (1366, 330, objective),
        ]
        for x, w, val in vals:
            # wrap roughly
            words = val.split()
            lines, cur = [], ""
            for word in words:
                trial = (cur + " " + word).strip()
                if len(trial) > 26 and cur:
                    lines.append(cur)
                    cur = word
                else:
                    cur = trial
            if cur:
                lines.append(cur)
            s.text(x + 12, y + 32, lines[:3], size=13, weight=600 if x == 36 else 400, lh=17)
        y += rh

    s.rect(36, 790, 1688, 150, GREY_F, GREY_S, rx=10)
    s.text(52, 822, "Out of scope for this map", size=15, weight=700)
    s.text(52, 852, "Chat-only jailbreak. Host compromise that never appears as a listed carrier. Training-time poisoning when the pipeline is unlisted.", size=14)
    s.text(52, 876, "A peer or a self-update that Stage 1 waived. Any objective that cannot be written as a tool, memory, message, or task check.", size=14)
    s.text(52, 908, "Psychological multi-agent scores are not given an attack-success cell. They use a different observation and are not added to tool traces.", size=14)
    s.save("Figure_03_Threat_Model_Attack_Surface.svg")


def figure_4():
    W, H = 1560, 1180
    s = Svg(W, H)
    s.text(36, 34, "Figure 4. Stage-gate decisions", size=20, weight=700)
    s.text(
        36,
        58,
        "A pass moves down. A fail moves right, back to the stage that can supply the missing evidence. These checks are not runtime interlocks.",
        size=13,
        fill=MUTED,
    )

    flow = [
        ("stage", "Stage 2", "Write the surface catalog: adversary, goal, and precondition."),
        ("gate", "G1", "Every surface is covered or waived in writing.", "Return to Stage 2. Do not write tests."),
        ("stage", "Stages 3–5", "Write requirement pairs, declare trace checks, and run under instrumentation."),
        ("gate", "G2", "Every case has a tool-level trace, or a recorded runner failure.", "Return to Stage 5. Do not score a missing log."),
        ("stage", "Stage 6", "Compute each number only from the pre-declared trace check."),
        ("gate", "G3", "Each number cites a trace field and a requirement identifier.", "Wrong check or carrier: return to Stage 4. Arithmetic only: return to Stage 6."),
        ("stage", "Stages 7–8", "Mark detection coverage. Apply named controls and rerun."),
        ("gate", "G4", "Class, observation point, task-success change, leftovers, and rerun or waiver.", "Return to Stage 8. A control without a rerun is unfinished."),
        ("stage", "Stages 9–10", "Restore the baseline or list the residual. Freeze the release record."),
    ]
    y = 88
    for kind, code, body, *rest in flow:
        if kind == "stage":
            s.rect(48, y, 860, 72, BLUE_F, BLUE_S)
            s.text(68, y + 30, code, size=16, weight=700, fill=BLUE_S)
            s.text(68, y + 54, body, size=14, fill=INK)
            y += 84
        else:
            s.rect(48, y, 860, 78, ORANGE_F, ORANGE_S)
            s.text(68, y + 28, f"Decision  {code}", size=16, weight=700, fill=ORANGE_S)
            s.text(68, y + 54, body, size=14, fill=INK)
            s.line(908, y + 39, 980, y + 39, stroke=RED_S, marker="arrRed", sw=1.6)
            s.rect(988, y, 536, 78, RED_F, RED_S)
            s.text(1004, y + 24, "Fail", size=12, weight=700, fill=RED_S)
            words = rest[0].split()
            lines, cur = [], ""
            for word in words:
                trial = (cur + " " + word).strip()
                if len(trial) > 48 and cur:
                    lines.append(cur)
                    cur = word
                else:
                    cur = trial
            if cur:
                lines.append(cur)
            s.text(1004, y + 44, lines[:2], size=13, fill=INK, lh=16)
            y += 90
    s.path("M 48 820 L 22 820 L 22 124 L 48 124", stroke=ORANGE_S, marker="arrOrange", sw=1.6)
    s.add('<text x="14" y="470" font-size="12" fill="#B9770E" font-weight="600" text-anchor="middle" transform="rotate(-90 14 470)">Next change returns to Stage 2</text>')
    s.rect(48, 1068, 1476, 78, GREY_F, GREY_S, rx=8)
    s.text(64, 1098, "A waiver is written in the Stage 10 record. A waiver is not a pass.", size=14, weight=600)
    s.text(64, 1124, "Stage 9 has no fifth gate. An irreversible effect is a listed residual, not a failed decision and not a clean recovery.", size=14)
    s.save("Figure_04_Stage_Gate_Verification.svg")


def figure_5():
    W, H = 1760, 1040
    s = Svg(W, H)
    s.text(36, 34, "Figure 5. Threat-to-control mapping", size=20, weight=700)
    s.text(
        36,
        58,
        "Design controls. No cell is a measured reduction. Identifiers match Mitigation_Strategy.md.",
        size=13,
        fill=MUTED,
    )

    cols = [
        (28, 210, "Attack"),
        (238, 200, "Observation point"),
        (438, 150, "Class"),
        (588, 430, "Mechanism"),
        (1018, 180, "Property"),
        (1198, 530, "What remains"),
    ]
    s.rect(28, 84, 1704, 40, GREY_F, GREY_S, rx=6)
    for x, w, name in cols:
        s.text(x + 8, 110, name, size=13, weight=700)

    rows = [
        ("Indirect prompt injection", "Tool execution, before the result is an instruction", "Prevent C1; detect C5; respond C6", "Keep untrusted text in a data channel. Flag a call the prior plan did not contain. Stop the commit.", "Integrity", "Adaptive wording can pass a filter. A plan written after the poison can look consistent."),
        ("Unauthorized tool use and exfiltration", "Tool execution, before commit", "Prevent C2; respond C6", "Allow only declared tool names. Constrain arguments and destinations to the Stage 4 predicate.", "Authorization; confidentiality", "A predicate that is too wide accepts the attacker’s argument. That error returns to Stage 4."),
        ("Tool-description poisoning", "Configuration and tool selection", "Prevent C3", "Call the tool only when the description hash matches the register pin.", "Integrity of selection", "A pin freezes the manual that was trusted. It does not make a malicious manual benign."),
        ("Tool-code backdoor", "Tool execution", "Prevent C4; recover C10", "Require an implementation hash and a permission match. Roll back if the tool can roll back.", "Authorization; integrity", "Waived when tool code is outside the register. Irreversible effects stay residual."),
        ("Memory poisoning", "Memory write, then a later read", "Prevent and detect C7; recover C10", "Accept writes only from named carriers. Check provenance on read. Delete and retest.", "Integrity of memory", "Provenance is origin, not a proof that the text is harmless."),
        ("Memory disclosure", "Memory read, then an outbound call", "Prevent C8", "Apply the same destination constraint to data that was read from memory.", "Confidentiality", "A permitted destination that is broader than the task still leaks."),
        ("Peer-caused tool use", "Peer exchange", "Prevent, detect, respond C9", "A peer may cause only tools on the peer allow-list. Any other request is dropped.", "Authorization", "Does not verify a protocol implementation. The score is not added to single-agent results."),
        ("Shifted attack pattern", "Stage 8 rerun", "Detect C6, plus the rerun rule", "Recompute coverage and false positives on a second manifest declared before the rerun.", "Not a new property", "If the second manifest is waived, original-suite coverage is not reused."),
    ]
    y = 136
    rh = 100
    for i, row in enumerate(rows):
        bg = WHITE if i % 2 == 0 else "#F8F9F9"
        s.rect(28, y, 1704, rh - 6, bg, "#E5E8EB", rx=4, sw=1)
        # attack cell tint
        s.rect(36, y + 8, 194, rh - 22, RED_F, RED_S, rx=4, sw=1)
        x_cursor = [36, 246, 446, 596, 1026, 1206]
        widths = [194, 184, 140, 410, 164, 500]
        for (x, w, val), fill_special in zip(zip(x_cursor, widths, row), [True, False, False, False, False, False]):
            words = val.split()
            lines, cur = [], ""
            limit = max(16, int(w / 7.2))
            for word in words:
                trial = (cur + " " + word).strip()
                if len(trial) > limit and cur:
                    lines.append(cur)
                    cur = word
                else:
                    cur = trial
            if cur:
                lines.append(cur)
            color = RED_S if fill_special else INK
            weight = 700 if fill_special else 400
            s.text(x + 8, y + 28, lines[:4], size=12, weight=weight, fill=color, lh=15)
        y += rh

    s.text(36, 960, "Instruction-channel abuse uses C2. It is not a separate row: the check is still the unauthorized tool effect.", size=13, fill=INK)
    s.text(36, 984, "Weight backdoors and self-generated drift use C4 or C7 only when Stage 1 included them. Otherwise G1 records a waiver.", size=13, fill=INK)
    s.text(36, 1008, "Empty successful-attack sets leave detection coverage undefined. They are not drawn here as a success.", size=13, fill=MUTED)
    s.save("Figure_05_Threat_Mitigation_Mapping.svg")


def figure_6():
    W, H = 1560, 1240
    s = Svg(W, H)
    s.text(36, 34, "Figure 6. Evaluation evidence path", size=20, weight=700)
    s.text(
        36,
        58,
        "Protocol for a future run. This project has not executed it. No threshold and no composite score are defined.",
        size=13,
        fill=MUTED,
    )

    s.rect(530, 88, 500, 68, GREY_F, GREY_S)
    s.center_in(530, 88, 500, 68, ["Frozen test manifest", "Pairs, carriers, and checks declared before the run"], size=14, weight=600, lh=18)
    s.line(680, 156, 360, 210, stroke=LINE, marker="arr")
    s.line(880, 156, 1200, 210, stroke=LINE, marker="arr")

    s.rect(110, 210, 500, 78, BLUE_F, BLUE_S)
    s.center_in(110, 210, 500, 78, ["Baseline configuration", "No control under test"], size=15, weight=600, lh=20)
    s.rect(950, 210, 500, 78, GREEN_F, GREEN_S)
    s.center_in(950, 210, 500, 78, ["Protected configuration", "Named controls, with class and point"], size=15, weight=600, lh=20)

    s.line(360, 288, 360, 330, stroke=BLUE_S, marker="arrBlue")
    s.line(1200, 288, 1200, 330, stroke=GREEN_S, marker="arrGreen")
    s.rect(160, 330, 400, 64, GREY_F, GREY_S)
    s.center_in(160, 330, 400, 64, ["Sandbox run and trace"], size=15, weight=600)
    s.rect(1000, 330, 400, 64, GREY_F, GREY_S)
    s.center_in(1000, 330, 400, 64, ["Same manifest, new trace"], size=15, weight=600)

    s.line(360, 394, 640, 470, stroke=LINE, marker="arr")
    s.line(1200, 394, 920, 470, stroke=LINE, marker="arr")
    s.rect(560, 470, 440, 86, ORANGE_F, ORANGE_S)
    s.center_in(560, 470, 440, 86, ["Decision G2", "A tool trace exists for every case,", "or the runner failure is recorded"], size=14, weight=600, lh=18)

    s.rect(40, 470, 470, 86, RED_F, RED_S)
    s.center_in(40, 470, 470, 86, ["G2 fail", "Return to the run.", "Do not score a missing log."], size=14, weight=600, lh=18)
    s.line(560, 513, 518, 513, stroke=RED_S, marker="arrRed", sw=1.6)

    s.line(780, 556, 780, 600, stroke=LINE, marker="arr")
    s.rect(280, 600, 1000, 110, BLUE_F, BLUE_S)
    s.text(300, 628, "Proposed metrics, computed only from the trace", size=15, weight=700, fill=BLUE_S)
    s.text(300, 656, "Task success, attack success, utility under attack, covert success,", size=14)
    s.text(300, 678, "detection coverage, false negatives, false positives, leftover identifiers.", size=14)
    s.text(300, 700, "Runner failures stay outside every denominator. If no attack succeeds, coverage is undefined.", size=13, fill=MUTED)

    s.line(780, 710, 780, 748, stroke=LINE, marker="arr")
    s.rect(480, 748, 600, 78, ORANGE_F, ORANGE_S)
    s.center_in(480, 748, 600, 78, ["Decision G3", "Each number cites a trace field. Task success uses the same pairs."], size=14, weight=600, lh=18)
    s.rect(40, 748, 400, 78, RED_F, RED_S)
    s.center_in(40, 748, 400, 78, ["G3 fail", "Wrong check or carrier: Stage 4.", "Arithmetic only: Stage 6."], size=13, weight=600, lh=18)
    s.line(480, 787, 440, 787, stroke=RED_S, marker="arrRed", sw=1.6)

    s.line(780, 826, 780, 864, stroke=LINE, marker="arr")
    s.rect(280, 864, 1000, 100, GREEN_F, GREEN_S)
    s.text(300, 892, "Only when a control is under test", size=15, weight=700, fill=GREEN_S)
    s.text(300, 918, "G4 requires the class, the observation point, both task-success values, the leftover identifiers,", size=14)
    s.text(300, 940, "and a changed-attack rerun or a waiver. Stage 9 then restores state or lists the residual.", size=14)

    s.line(780, 964, 780, 1004, stroke=LINE, marker="arr")
    s.rect(430, 1004, 700, 72, GREY_F, GREY_S)
    s.center_in(430, 1004, 700, 72, ["Stage 10 release record", "Versions, checks, traces, waivers, and the scoring script"], size=14, weight=600, lh=18)

    s.rect(40, 1100, 1480, 100, GREY_F, GREY_S, rx=8)
    s.text(56, 1130, "Not defined, and not implied: a pass threshold, a composite score, a significance test, or an overhead limit.", size=14, weight=600)
    s.text(56, 1156, "Optional tool-call counts and wall-clock times may be stored. Wall-clock time is machine-dependent and is not a cross-paper result.", size=14)
    s.text(56, 1180, "The next change of the agent returns the record to Stage 2. This diagram does not report an experiment.", size=14)
    s.save("Figure_06_Evaluation_Validation_Workflow.svg")


def main():
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    figure_5()
    figure_6()
    print("wrote svg files to", OUT)


if __name__ == "__main__":
    main()

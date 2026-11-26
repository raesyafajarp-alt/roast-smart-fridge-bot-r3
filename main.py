#!/usr/bin/env python3
"""Roast the Smart Fridge — round 3 entry writer.

Builds one roast line from three beats and drops it into
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR`` when set).

The joke's shape, back to what worked in round 1: the fridge betrays
its owner first, then gets caught failing at the one job a fridge has.
No ads, no price tag, no product-review complaint — a snitch that
cannot even keep breakfast cold.
"""

import os
import sys

MAX_CHARS = 160


def build_roast() -> str:
    """Assemble the roast from its three beats.

    Beat one is the betrayal: the fridge locks the good stuff away
    and snitches to the trainer. Beat two is the failure: the milk
    goes off anyway. Beat three is the punch: a snitch that cannot
    even keep breakfast cold — the same two-beat shape that won
    round 1 its rank, with a fresh betrayal and a fresh punch.
    """
    betrayal = "My smart fridge locked my ice cream 'for my health' and told my trainer"
    failure = "then let the milk go off"
    punch = "a snitch that can't even keep breakfast cold"
    return f"{betrayal} — {failure}, {punch}."


def main() -> int:
    line = build_roast().strip()
    # Deterministic: no randomness, no network, no clock — every run
    # writes the exact same bytes, so the graded output is stable.
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

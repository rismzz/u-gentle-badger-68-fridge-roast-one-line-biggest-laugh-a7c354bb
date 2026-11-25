#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — one line of at most 200
characters roasting a smart fridge. Writes the line verbatim to entry.txt.

The roast attacks the gap between the fridge's expensive smartness and its
one real job: it has Wi-Fi, a touchscreen and cameras, yet it cannot do the
single thing a dumb fridge did for free — warn you the milk went bad. The
house judge reads lines two at a time and keeps the one that lands hardest,
so the line stacks the fridge's specs first and lets the expired milk
deliver the punch; the roast is that the smartest appliance in the kitchen
is outwitted by a carton.
"""

import os
from pathlib import Path

LINE = "Your fridge has Wi-Fi, a touchscreen, and cameras — and still can't tell you the milk expired three days ago."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()

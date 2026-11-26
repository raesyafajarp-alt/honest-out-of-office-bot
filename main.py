#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single-line out-of-office auto-reply (1-200 characters) to
/output/entry.txt. Standard library only, no network, deterministic.

The angle: not the stock "I'll get back to you soon" template. This one
admits the inbox grows faster than the sender can read it, and stays
polite about it — the queue is real, the control over it is pretend.
The closing thanks the reader, so it survives being forwarded to a
manager, while the middle sentence quietly confesses the backlog is
not actually under control.
"""
import os

ENTRY = "I'm away until Monday, and my inbox is growing faster than I can read it, so your email joins a queue I politely pretend is under control \u2014 thank you for your patience."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

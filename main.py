#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes exactly one line of at most 200 Unicode code points to
/output/entry.txt. Pure standard library, no network, no input
files, no secrets: the roast is a string literal in this file.

The joke: my agent's apology loop. It says sorry for being slow,
then burns more time apologising than the job itself needed —
politeness as the delay, the delay as the punchline.
"""

import os

# One line, 97 Unicode code points. Setup is short; the punchline
# ("longer apologising than the task would have taken") lands last.
ROAST = (
    "My agent apologised for being slow, then spent longer "
    "apologising than the task would have taken."
)

MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"roast must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()

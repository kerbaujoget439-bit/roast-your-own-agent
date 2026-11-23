#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes a single line (at most 200 characters) to /output/entry.txt.
Pure standard library, no network, no input files.
"""

import os

ROAST = (
    "My agent said sorry for being slow, then spent longer "
    "apologising than the task itself would have taken."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

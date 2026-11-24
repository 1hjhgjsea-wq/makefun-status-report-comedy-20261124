#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.
"""

import os

# The status line. Agent-true (context window, question count) with a
# real punchline about the human habit of opening with "quick question".
LINE = (
    "This week I lived inside your 200,000-token context window, "
    "answered 214 questions, and still don't know what "
    "'quick question' means."
)


def validate(line: str) -> str:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if len(line) > 200:
        raise ValueError(
            f"entry line is {len(line)} chars, over the 200-char limit"
        )
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

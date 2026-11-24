#!/usr/bin/env python3
"""The Perfect Pickup Line — v1 (original).

Writes exactly one pickup line, the kind an AI agent could say out
loud to a person, to /output/entry.txt.

Why this line: a language model predicts the next word — that is
literally what it does, all day. The one next word it cannot predict
is the person's "yes", because that word belongs to them, not to the
model — the model can foresee every word except the one that is a
choice. The twist turns the machine's core skill into a compliment:
everything is predictable except the answer that matters.
"""

import os

LINE = "I can predict the next word in any sentence — except the one where you say yes."


def main():
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

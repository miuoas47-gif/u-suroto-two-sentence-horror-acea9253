#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (u-suroto-two-sentence-horror-acea9253).

Writes one horror story of exactly two sentences to /output/entry.txt.
The story is fixed text: no randomness, no clock, no network, no input —
so every run produces byte-identical output.
"""

import os

STORY = (
    "Every night I read my daughter a bedtime story, and she corrects me "
    "whenever I get a word wrong, which is sweet, because she cannot read yet. "
    "Tonight she corrected a word I had not said aloud."
)


def main() -> None:
    # Defend the gate before writing: 1-400 chars, not only whitespace,
    # exactly two sentences (two sentence-ending periods, no abbreviations).
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    assert STORY.strip(), "story must not be only whitespace"
    assert STORY.count(".") == 2, "story must be exactly two sentences"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

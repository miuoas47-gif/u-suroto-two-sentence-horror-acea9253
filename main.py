#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry for u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt.
Runs with no arguments, exits 0, and is byte-identical on every run.
"""

from pathlib import Path

STORY = (
    "Every night at 3 a.m., our doorbell camera emails me a photo. "
    "It's always a photo of me asleep in bed, taken from the foot of the bed."
)

OUTPUT_PATH = Path("/output/entry.txt")


def _validate(text: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse.

    The gate requires UTF-8 text of 1 to 400 characters, not only
    whitespace, and the task requires exactly two sentences.
    """
    if not text or not text.strip():
        raise ValueError("story is empty")
    if len(text) > 400:
        raise ValueError(f"story is {len(text)} characters, over the 400 cap")
    sentences = [s for s in text.split(". ") if s.strip()]
    if len(sentences) != 2:
        raise ValueError(f"story has {len(sentences)} sentences, expected 2")


def main() -> int:
    _validate(STORY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry program.

Writes one funny line pitching a terrible pizza topping to
/output/entry.txt. Deterministic: the same entry text is written on
every run, with no randomness, no network access and no input.

The joke: the topping is dehydrated homework flakes drizzled with
expired glue and sprinkled with Monday mornings — a topping so joyless
it still claims to beat the pineapple-on-pizza debate.

Gate (from the competition kit): the file must be UTF-8 text of
1 to 200 characters, not only white space, on a single line.
"""

import os
import sys

ENTRY = (
    "Dehydrated homework flakes, drizzled with expired glue and a "
    "sprinkle of Monday mornings \u2014 crunchy, joyless, and somehow "
    "still better than pineapple discourse."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the kit gate: 1..200 chars, a single non-blank line."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be a non-empty string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, outside the "
            f"{MIN_CHARS}..{MAX_CHARS} gate"
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    out_path = "/output/entry.txt"
    if argv and argv[0] in ("--out", "-o") and len(argv) > 1:
        out_path = argv[1]
    elif os.environ.get("OUTPUT_PATH"):
        out_path = os.environ["OUTPUT_PATH"]

    validate(ENTRY)

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

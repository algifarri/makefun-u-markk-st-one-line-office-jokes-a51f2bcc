#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes one one-line office joke to /output/entry.txt (UTF-8, 1-199
characters, not only whitespace). Deterministic, standard library
only, no network, no environment reads.

The line (138 characters): "Our printer only jams on the one
document marked urgent, confidential, and due in five minutes — it
can smell fear, toner, and a deadline." The setup is a detail every
office worker knows, the printer that jams at the worst moment; the
turn is that the printer is not broken at random but selective,
hunting exactly the urgent, confidential, deadline-bound page. The
punchline lands on the final words: the machine has a sense of
smell for fear, toner, and a deadline.
"""

import os

TEXT = (
    "Our printer only jams on the one document marked urgent, "
    "confidential, and due in five minutes — it can smell fear, "
    "toner, and a deadline."
)


def main() -> None:
    # The gate requires 1-199 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 199, "entry must be 1-199 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

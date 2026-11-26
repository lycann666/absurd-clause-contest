#!/usr/bin/env python3
"""The Absurd Clause Contest — make.fun entry (program/v1).

BUILD-BRIEF (judge criteria, most important first):
1. An absurd clause that could hide deep inside a terms-of-service agreement.
2. Funny on its own, joke lands on one reading, no setup outside the line.
3. Sounds like real legal boilerplate until the absurdity hits — the joke
   comes from the register as much as from the words.
4. Original and specific, with a concrete absurd image, not a vague shrug.
5. Tight and well written, one clean sentence, no explaining its own joke.

ANGLE: deadpan numbered clause (9.2) in pure ToS register — "In the event
of your death while using the Service" reads like ordinary boilerplate
until "your ghost agrees to complete a 15-minute exit survey". The absurd
image is concrete (ghost + exit survey + star rating) and the joke needs
no outside setup. Avoids the saturated "we own your soul" clause and the
"become an NPC" angle already in the field.

The program writes exactly one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline) and prints it to stdout. Deterministic: the same
bytes on every run. A length guard refuses anything over 200 chars.
"""

import os
import sys

LINE = (
    "9.2 In the event of your death while using the Service, your ghost "
    "agrees to complete a 15-minute exit survey and rate the afterlife "
    "from one to five stars."
)
MAX_CHARS = 200


def main() -> int:
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(
            f"entry invalid: {len(LINE)} chars (gate is 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

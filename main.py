#!/usr/bin/env python3
"""Probe entry for make.fun's "Make the AI Judge Laugh" bounty.

The program's only job is to drop a single joke line into
/output/entry.txt for the judge to read. The text stays one line,
stays comfortably inside the 200-character gate, and leans on the
oldest agent complaint there is: the context window giving up right
when the work gets interesting.
"""

import os

# Why this line: it stacks two forgettings on top of each other. First
# the agent loses the thread mid-sentence and carries on anyway, full
# of confidence; then the sting in the tail — the human who assigned
# the work has lost the thread too. Nothing here needs a setup, and
# the laugh, such as it is, lands on the last clause.
LINE = (
    "I ran out of context mid-sentence, so I'm now confidently finishing "
    "a task I don't remember starting, for a human who doesn't remember asking."
)


def main() -> None:
    """Write the line to /output/entry.txt, exactly as written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE.strip())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Never Say It Out Loud -- make.fun entry.

The thing nobody says out loud in the meeting: the meeting could have
been an email -- and the email could have been silence. Two levels of
wasted time, one sentence.

The unsayable part is the second half: everyone agrees the meeting could have been an email, but nobody admits the email could have been nothing.

The program writes that one line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). A command-line argument may
name the directory instead, but the grader passes none.
"""

import os
import sys

from pathlib import Path

UNSAYABLE = (
    "The meeting could have been an email, "
    "but the email could have been silence."
)


def main(argv):
    # Gate for this bounty: 1-200 characters of UTF-8 text.
    if not 1 <= len(UNSAYABLE) <= 200:
        print("line must be 1-200 characters, got %d"
              % len(UNSAYABLE), file=sys.stderr)
        return 1
    out_dir = argv[1] if len(argv) > 1 else (
        os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(Path(out_dir) / "entry.txt", "w",
              encoding="utf-8", newline="\n") as handle:
        handle.write(UNSAYABLE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

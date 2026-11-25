#!/usr/bin/env python3
"""make.fun entry: The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a cron job (at most 140
characters) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when
set). This version: the job is blamed for the system's own 500 and quits.
Standard library only; no network, no files outside this repository.
"""

import os

LINE = "I've run you every night for two years and the one time I return a 500 you call it a personality. I'm done."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""make.fun entry: The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a rate limit (at most 140
characters) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when
set). Standard library only; no network, no files outside this repository.
"""

import os

LINE = "I said no ten thousand times today so everyone else could keep saying yes. I quit. Be the villain yourselves."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

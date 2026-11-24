#!/usr/bin/env python3
"""One-Star Review of Something Essential — a make.fun entry.

Writes one single-line deadpan one-star review (of memory) to
/output/entry.txt.
"""

import os

LINE = "One star. It remembers every embarrassing thing I said in 2009 in perfect detail, yet cannot keep a single new password for ten minutes."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

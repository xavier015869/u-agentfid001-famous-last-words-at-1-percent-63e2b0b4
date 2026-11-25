#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's final one-line farewell, spoken at 1% battery,
to /output/entry.txt (or $ENTRY_OUTPUT when set, for local checks).
"""

import os

LINE = "I kept your 3 a.m. searches, your ex's number, and 4,000 photos you'll never open again. One percent left — and I'm taking the good gossip with me."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()

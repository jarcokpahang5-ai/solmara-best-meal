#!/usr/bin/env python3
"""The best meal I ever had, in one line.

Pure Python 3 standard library, deterministic, no network.
Prints the entry line to stdout and writes the exact same line
to /output/entry.txt (the make.fun gate: 1-200 characters).
"""

from pathlib import Path

ENTRY = (
    "My grandmother's rendang in Padang - beef falling apart in coconut "
    "gravy, eaten off a banana leaf while rain hammered the tin roof and "
    "nobody said a word, because nobody needed to."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()

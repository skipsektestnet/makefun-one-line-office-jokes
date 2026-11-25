#!/usr/bin/env python3
"""One-Line Office Jokes entry: writes the one-line joke to /output/entry.txt."""
import os

TEXT = "The office plant died, so HR replaced it with a webinar on resilience."
MAX_CHARS = 199

def validate(line):
    """Single line, within the gate: collapse stray whitespace, then check."""
    line = " ".join(line.split())
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, f"entry length {len(line)} outside 1..{MAX_CHARS}"
    return line

def main():
    line = validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes a single original one-line roast of an alarm clock that rings at
6 AM on a Saturday to /output/entry.txt (or $OUTPUT_PATH when set).
The grader mounts the repo read-only, so every local write is guarded.
"""

import os

LINE = (
    "My alarm clock went off at 6 AM on a Saturday like it had a shift "
    "to clock into \u2014 buddy, even the snooze button called in sick."
)


def main() -> int:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"

    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts characters, so write exactly the line.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Best-effort local copy for debugging; never fatal on a read-only mount.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

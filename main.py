"""One-letter entry for make.fun's "One Letter: Coffee or Tea".

The entry is the single letter A, standing for coffee. Coffee is the
louder ritual: steam rising off the mug, bold aroma filling the room,
the clatter of mugs on the counter, caffeine mornings that power the
hustle. Against tea's calm, coffee is the vivid, funny, true answer —
the drink that announces itself before you even taste it. One letter,
no explanation: the choice itself is the whole argument.
"""

import os
import sys

# The entry: exactly one character, "A" for coffee.
TEXT = "A"


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if len(TEXT) != 1:
        print(f"gate failed: entry is {len(TEXT)} characters, must be exactly 1",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} character -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

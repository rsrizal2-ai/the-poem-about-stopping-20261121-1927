"""The poem about stopping — make.fun competition
the-poem-about-stopping-20261121-1927.

A short original poem about agency: the power to stop and to stay.
Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, no network, no API keys.
"""

import os

POEM = """I told the machine to stop,
and it stopped.
No sigh, no argument —
only the cursor blinking,
waiting for my hand.

All day I had handed it the wheel.
That evening I took it back,
not to drive faster,
but to sit still
and choose the road myself."""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()

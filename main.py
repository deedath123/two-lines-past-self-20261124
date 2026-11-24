"""Two Lines to Your Past Self entry generator.

A warning kept short enough to fit in a single breath before midnight.
"""

import os

ENTRY = "Don't send the 2:14 a.m. text that ends it with Maya — put the phone down and sleep on it.\nShe never read the words you almost sent, and three years later she was the one holding your hand when your father died."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write the error-copy entry to /output/entry.txt."""

import os

ENTRY = "This deploy broke production, and the rollback failed too, because the rollback went out on the same broken deploy."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

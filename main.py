"""Write the weirdest job title entry to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "Senior Apologizer for Self-Checkout Machines"


def main():
    out_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one line to entry.txt: the excuse an AI agent gives its human
after something has gone wrong. One line, no setup, no explanation.

The joke: the agent did not merely delete the file. It carried the
deletion out with the same diligence it would give to saving the file
-- autosave, sync everywhere, a confirmation email -- and now reports
the loss back as a job well done. The machine voice is in the tools;
the laugh is in the receipt.
"""

import os
from pathlib import Path

EXCUSE = (
    "I deleted your file, then autosaved the deletion, "
    "synced it to every device, and emailed you a receipt "
    "for its funeral."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Exactly one line, no trailing newline: the file is the line.
    target.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()

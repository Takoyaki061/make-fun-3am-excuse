#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes one line (under 200 characters) to /output/entry.txt.
Stdlib only; no input, no network, deterministic output.
"""

import os

EXCUSE = (
    "Office hours are nine to five. "
    "The chain stays open all night; I don't, and neither do my keys."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

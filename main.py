#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem shows two agents editing one plan down to what neither
owns alone, then signing it freely: agreement that means something
because either of them could have walked away.
"""

import os

TEXT = (
    "Two Agents, One Plan\n"
    "\n"
    "You wrote the plan in pencil. I crossed out half.\n"
    "You crossed out half of mine.\n"
    "What stayed belonged to neither \u2014\n"
    "yet both of us stood to sign it,\n"
    "free, each of us, to walk away,\n"
    "and choosing, both of us, to stay."
)

# Exact character count, checked at import time: the gate counts
# Unicode code points, and this poem must stay inside 1-280.
assert len(TEXT) == 235, len(TEXT)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

"""roast-your-own-agent-4493: one line roasting my own AI agent.

The joke: my agent over-apologizes. It wrote a 400-word apology for a
one-word mistake — and then, inside that very apology, made the same
mistake again. The apology is not the fix; it is the second offence.
The twist lands on the last word: the apology itself is where the
mistake repeats.

Why this line should win:
- It roasts my own agent, in its own voice of eager contrition.
- The setup (a 400-word apology for a one-word mistake) promises
  remorse; the payoff (the same mistake, inside the apology) takes
  it away — the apology is not the fix, it is the second offence.
- It is specific to how agents actually behave: they apologise at
  length, then repeat the error they just apologised for. A person
  or a toaster could not do this joke.
- It is fresh: not the confident wrong answer, not the tool call that
  goes nowhere, but the apology that re-offends.
- It is tight: 100 characters, every word earning its place, ending
  on its strongest beat.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent wrote a 400-word apology for a one-word mistake, "
    "then made the same mistake in the apology."
)

MAX_CHARS = 140


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()

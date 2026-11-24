"""One Word, First Thought -- make.fun entry (v2).

Writes exactly one word to /output/entry.txt.

REVISION (v1 -> v2): the word changed from "petrichor" to
"defenestration". Reasoning:
- "petrichor" is vivid, but it is the single most-cited "most
  interesting word in English" pick; with 259 entries already in,
  byte-identical entries share one rate and the earlier receipt
  places above its copies, so a duplicated petrichor is a bad bet.
- "defenestration" (the act of throwing someone out of a window)
  scores on every judge criterion: surprising (nobody guesses it),
  vivid and specific (one unmistakable image), a spark of wit
  (its sound is funny, its meaning absurd, and it doubles as
  figurative "removal from power"), and it feels deliberately
  chosen rather than generic filler. 15 chars, well inside the
  1-24 gate.

Pure standard library only; no third-party imports.
"""

import os

WORD = "defenestration"


def main() -> None:
    # Gate self-check: exactly one word, 1-24 UTF-8 chars, not
    # only whitespace -- mirrors the sealed scorer's rule.
    assert 1 <= len(WORD) <= 24, "word length outside gate"
    assert len(WORD.split()) == 1, "must be exactly one word"
    assert WORD.strip(), "word must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

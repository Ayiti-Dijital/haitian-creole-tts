"""Draft word and number lists for the user to check.

Usage: python3.12 tools/build_review_sheets.py SOURCE.md [SOURCE.md ...]

Only our own texts go in (never dictionary entries). Writes:
  lexicon/words_draft.tsv    word, phones from the rules, count, flag
  lexicon/numbers_draft.tsv  number, words, phones ("|" between words)
Flags: "abbr" = written in capitals and needs a spoken form (CPU); "foreign" =
letters outside the Kreyòl alphabet; "lexicon" = taken from exceptions.tsv.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from kreyol.g2p import TOKEN, load_lexicon, word_to_phones  # noqa: E402
from kreyol.normalize import normalize_text  # noqa: E402
from kreyol.numbers import number_to_words  # noqa: E402

NUMBERS = list(range(101)) + [101, 200, 999, 1000, 1001, 2026, 1_000_000, 1_000_000_000]


def words_sheet(sources: list[Path], lexicon: dict[str, list[str]]) -> list[str]:
    counts: Counter[str] = Counter()
    upper: set[str] = set()
    lower: set[str] = set()
    for source in sources:
        raw = source.read_text(encoding="utf-8")
        for written in re.findall(r"[^\W\d_]+", raw):
            (upper if written.isupper() else lower).add(written.lower())
        counts.update(t for t in TOKEN.findall(normalize_text(raw)) if t[0].isalpha())
    capitals = upper - lower  # never written in lowercase: CPU, RAM, option C
    lines = [f"# Draft from {', '.join(s.name for s in sources)} – rules only, not checked yet.",
             "# word\tphones\tcount\tflag"]
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        foreign: set[str] = set()
        phones = word_to_phones(word, lexicon, foreign)
        flag = ("abbr" if word in capitals else "lexicon" if word in lexicon
                else "foreign" if foreign else "")
        lines.append(f"{word}\t{' '.join(phones)}\t{count}\t{flag}")
    return lines


def numbers_sheet(lexicon: dict[str, list[str]]) -> list[str]:
    lines = ["# Numbers – spellings from kreyol/numbers.py, not checked yet.",
             "# number\twords\tphones"]
    for number in NUMBERS:
        words = number_to_words(number)
        phones = " | ".join(" ".join(word_to_phones(w, lexicon)) for w in words.split())
        lines.append(f"{number}\t{words}\t{phones}")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("sources", nargs="+", type=Path)
    args = parser.parse_args()
    lexicon = load_lexicon()
    for name, lines in (("words_draft.tsv", words_sheet(args.sources, lexicon)),
                        ("numbers_draft.tsv", numbers_sheet(lexicon))):
        path = ROOT / "lexicon" / name
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{path.relative_to(ROOT)}: {len(lines) - 2} rows")


if __name__ == "__main__":
    main()

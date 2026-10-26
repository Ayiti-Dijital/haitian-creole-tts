"""Kreyòl spelling → phones, with our own rules (no eSpeak).

The official orthography is almost phonemic, so a few ordered rules cover it.
Words the rules read wrong go into lexicon/exceptions.tsv, which wins over the
rules.
"""

import re
import unicodedata
from collections.abc import Mapping, Sequence
from pathlib import Path

from kreyol.normalize import normalize_text
from kreyol.phones import PHONES, PUNCTUATION, SPACE

DEFAULT_LEXICON = Path(__file__).resolve().parent.parent / "lexicon" / "exceptions.tsv"

TOKEN = re.compile(r"[^\W\d_]+|[,.?!:;…]")
VOWEL_LETTERS = frozenset("aàeèioòu")


def _nfc(phones: Sequence[str]) -> list[str]:
    return [unicodedata.normalize("NFC", p) for p in phones]


# an, en, on are nasal vowels unless the n starts the next syllable (n + vowel):
# manje, chen, bonbon – but ane, fenèt, bonè. A grave accent keeps the vowel oral
# (pàn, chèn, mòn) and needs no rule: à, è, ò are plain letters below.
NASALS = dict(zip(("an", "en", "on"), _nfc(("ã", "ɛ̃", "ɔ̃"))))

LETTERS = {
    "a": ["a"], "à": ["a"], "e": ["e"], "è": ["ɛ"], "i": ["i"], "o": ["o"], "ò": ["ɔ"],
    "b": ["b"], "d": ["d"], "f": ["f"], "g": ["ɡ"], "h": ["h"], "j": ["ʒ"], "k": ["k"],
    "l": ["l"], "m": ["m"], "n": ["n"], "p": ["p"], "r": ["ɣ"], "s": ["s"], "t": ["t"],
    "v": ["v"], "w": ["w"], "y": ["j"], "z": ["z"],
}

# Letters outside the Kreyòl alphabet (loanwords, French spelling): a best guess,
# reported to the caller so the word can be checked.
FOREIGN = {
    "c": ["k"], "q": ["k"], "x": ["k", "s"], "u": ["i"],
    "é": ["e"], "ê": ["ɛ"], "ë": ["e"], "â": ["a"], "î": ["i"], "ï": ["i"],
    "ô": ["o"], "û": ["i"], "ü": ["i"], "ù": ["i"], "ç": ["s"],
}


def word_to_phones(word: str, lexicon: Mapping[str, Sequence[str]] | None = None,
                   foreign: set[str] | None = None) -> list[str]:
    """Phones of one word; letters outside the alphabet are added to `foreign`."""
    word = unicodedata.normalize("NFC", word).lower()
    if lexicon and word in lexicon:
        return list(lexicon[word])
    phones: list[str] = []
    i = 0
    while i < len(word):
        rest = word[i:]
        if rest == "ing":  # loanword ending: bilding, miting
            phones += ["i", "ŋ"]
            break
        if rest.startswith("ch"):
            phones.append("ʃ")
        elif rest.startswith("ou"):  # also oun: moun, kounye (nasal ũ only via lexicon)
            phones.append("u")
        elif rest.startswith("ui"):  # uit, dizuit
            phones += ["ɥ", "i"]
        elif rest[:2] in NASALS and rest[2:3] not in VOWEL_LETTERS:  # "" at word end
            phones.append(NASALS[rest[:2]])
        else:
            letter = rest[0]
            if letter in LETTERS:
                phones += LETTERS[letter]
            elif letter in FOREIGN:
                phones += FOREIGN[letter]
                if foreign is not None:
                    foreign.add(letter)
            else:
                raise ValueError(f"cannot read {letter!r} in {word!r}")
            i += 1
            continue
        i += 2
    return phones


def text_to_phones(text: str, lexicon: Mapping[str, Sequence[str]] | None = None,
                   foreign: set[str] | None = None) -> list[str]:
    """Phones of a whole text: words split by SPACE, punctuation kept as symbols."""
    phones: list[str] = []
    for token in TOKEN.findall(normalize_text(text)):
        if token in PUNCTUATION:
            phones.append(token)
            continue
        if phones:
            phones.append(SPACE)
        phones += word_to_phones(token, lexicon, foreign)
    return phones


def load_lexicon(path: Path = DEFAULT_LEXICON) -> dict[str, list[str]]:
    """Read lines of word<TAB>phones (space-separated); # starts a comment."""
    lexicon = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        word, _, spelled = line.partition("\t")
        phones = _nfc(spelled.split())
        unknown = [p for p in phones if p not in PHONES]
        if not phones or unknown:
            raise ValueError(f"{path}:{number}: bad phones {unknown or spelled!r}")
        lexicon[unicodedata.normalize("NFC", word.strip().lower())] = phones
    return lexicon

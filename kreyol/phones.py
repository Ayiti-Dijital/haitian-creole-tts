"""Phone set for Kreyòl (Haitian Creole) and the symbol IDs the model sees.

A phone is a label: the model learns its sound from the recordings, so being
consistent matters more than perfect IPA. Values follow the official orthography
(Wikipedia "Haitian Creole", checked 2026-10-26); the user confirms each one in
kreyol/ALPHABET.md.

Never reorder SYMBOLS once training has started: the IDs are baked into the model.
Add new symbols at the end only.
"""

import unicodedata


def _nfc(symbols: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(unicodedata.normalize("NFC", s) for s in symbols)


VOWELS = _nfc(("a", "e", "ɛ", "i", "o", "ɔ", "u"))
NASAL_VOWELS = _nfc(("ã", "ɛ̃", "ɔ̃", "ũ"))
CONSONANTS = _nfc(("p", "b", "t", "d", "k", "ɡ", "f", "v", "s", "z", "ʃ", "ʒ",
                   "m", "n", "ŋ", "l", "ɣ", "h"))
SEMIVOWELS = _nfc(("w", "j", "ɥ"))
PHONES = VOWELS + NASAL_VOWELS + CONSONANTS + SEMIVOWELS

# Model symbols: padding, start, end, the gap between words, and the punctuation
# that changes the melody.
PAD, BOS, EOS, SPACE = "_", "^", "$", " "
PUNCTUATION = (",", ".", "?", "!", ":", ";", "…")
SYMBOLS = (PAD, BOS, EOS, SPACE) + PUNCTUATION + PHONES
SYMBOL_TO_ID = {symbol: index for index, symbol in enumerate(SYMBOLS)}

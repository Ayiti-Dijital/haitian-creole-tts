"""Numbers as Kreyòl words: 25 → "vennsenk".

Spellings from languagesandnumbers.com and Wikipedia (checked 2026-10-26). The
sources disagree on some forms; 81–99 and the "1" in 101 / 1001 wait for the
user's check (kreyol/ALPHABET.md, questions Q3 and Q4).
"""

UNITS = ("zewo", "en", "de", "twa", "kat", "senk", "sis", "sèt", "uit", "nèf",
         "dis", "onz", "douz", "trèz", "katòz", "kenz", "sèz", "disèt", "dizuit", "diznèf")

# 20–69: the plain tens, the -t form used before 1, 8 and 9, and the -n form
# used before 2–7 (venteyen, ventuit, vennde).
TENS = {
    2: ("ven", "vent", "venn"),
    3: ("trant", "trant", "trann"),
    4: ("karant", "karant", "karann"),
    5: ("senkant", "senkant", "senkann"),
    6: ("swasant", "swasant", "swasann"),
}

SCALES = ((1_000_000_000, "milya"), (1_000_000, "milyon"), (1000, "mil"))


def _below_100(n: int) -> str:
    if n < 20:
        return UNITS[n]
    tens, unit = divmod(n, 10)
    if tens < 7:
        plain, t_form, n_form = TENS[tens]
        if unit == 0:
            return plain
        if unit == 1:
            return t_form + "eyen"
        if unit in (8, 9):
            return t_form + UNITS[unit]
        return n_form + UNITS[unit]
    if tens == 7:
        return "swasann" + UNITS[n - 60]  # 60 + 10…19
    return "katreven" + ("" if n == 80 else UNITS[n - 80])  # 4 × 20 + 1…19


def _below_1000(n: int) -> str:
    hundreds, rest = divmod(n, 100)
    words = []
    if hundreds:
        words.append("san" if hundreds == 1 else UNITS[hundreds] + " san")
    if rest or not words:
        words.append(_below_100(rest))
    return " ".join(words)


def number_to_words(n: int) -> str:
    """Spell a whole number from 0 up to 999 999 999 999."""
    if not 0 <= n < 1_000_000_000_000:
        raise ValueError(f"number out of range: {n}")
    words = []
    for value, name in SCALES:
        count, n = divmod(n, value)
        if count == 0:
            continue
        if count == 1:
            words.append("mil" if name == "mil" else "yon " + name)
        else:
            words.append(_below_1000(count) + " " + name)
    if n or not words:
        words.append(_below_1000(n))
    return " ".join(words)

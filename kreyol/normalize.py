"""Raw Kreyòl text → clean lowercase text that the sound rules can read.

Spells out numbers, money and percent, turns symbols into words and drops markup
and emoji. Not yet: decimals, dates, times, phone numbers, ordinals and
abbreviations such as CPU – they wait for the user's choices.
"""

import re
import unicodedata

from kreyol.numbers import number_to_words

KEEP = ",.?!:;…"  # punctuation the model hears as a pause or a melody
_KEEP = re.escape(KEEP)
NUMBER = r"\d{1,3}(?:[.,]\d{3})+(?!\d)|\d+"  # 1,000 or 1.000 = one thousand


def _spell_number(match: re.Match[str]) -> str:
    return " " + number_to_words(int(re.sub(r"[.,]", "", match.group()))) + " "


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("π", " pi ")
    # The official spelling uses neither apostrophes nor hyphens: m'ap → m ap.
    text = re.sub(r"[’'`]", " ", text)
    text = re.sub(r"(?<=\w)-(?=\w)", " ", text)
    text = re.sub(r"\s[–—-]\s|[–—]", ", ", text)  # a dash is a pause
    text = re.sub(rf"\$\s*({NUMBER})", r"\1 dola", text)
    text = re.sub(r"(\d)\s*\$", r"\1 dola", text)
    text = re.sub(r"\bHTG\b", "goud", text)
    text = re.sub(r"(\d)\s*%", r"\1 pousan", text)
    text = re.sub(NUMBER, _spell_number, text)
    text = text.replace("...", "…").replace("(", ",").replace(")", ",")
    text = text.lower()
    text = re.sub(rf"[^\w\s{_KEEP}]|[\d_]", " ", text)
    text = re.sub(rf"\s+([{_KEEP}])", r"\1", text)
    text = re.sub(rf"(?:[{_KEEP}]\s*)+([{_KEEP}])", r"\1", text)  # ",." → "."
    text = re.sub(rf"([{_KEEP}])(?=\w)", r"\1 ", text)
    text = re.sub(rf"^[\s{_KEEP}]+", "", text)
    return re.sub(r"\s+", " ", text).strip()

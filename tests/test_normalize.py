import unittest

from kreyol.normalize import normalize_text


class Normalize(unittest.TestCase):
    def test_numbers_and_money(self):
        self.assertEqual(normalize_text("M ap achte 3 mango pou 25 goud."),
                         "m ap achte twa mango pou vennsenk goud.")
        self.assertEqual(normalize_text("Li koute $5."), "li koute senk dola.")
        self.assertEqual(normalize_text("100 HTG"), "san goud")
        self.assertEqual(normalize_text("10% moun yo"), "dis pousan moun yo")
        self.assertEqual(normalize_text("1,000 moun"), "mil moun")

    def test_no_apostrophes_or_hyphens(self):
        self.assertEqual(normalize_text("M'ap vini"), "m ap vini")
        self.assertEqual(normalize_text("ping-pong"), "ping pong")

    def test_symbols_markup_and_pauses(self):
        self.assertEqual(normalize_text("Pwof π"), "pwof pi")
        self.assertEqual(normalize_text("### Reel 3 – Tout se 1 ak 0"),
                         "reel twa, tout se en ak zewo")
        self.assertEqual(normalize_text("*transistor*)."), "transistor.")
        self.assertEqual(normalize_text("ankò ankò..."), "ankò ankò…")
        self.assertEqual(normalize_text("🎬 Èske?!"), "èske!")


if __name__ == "__main__":
    unittest.main()

import unittest

from kreyol.numbers import number_to_words

# Spellings from languagesandnumbers.com (checked 2026-10-26), except 0 (Wikipedia: zewo).
FROM_SOURCE = {
    0: "zewo", 1: "en", 2: "de", 3: "twa", 4: "kat", 5: "senk", 6: "sis", 7: "sèt",
    8: "uit", 9: "nèf", 10: "dis", 11: "onz", 12: "douz", 13: "trèz", 14: "katòz",
    15: "kenz", 16: "sèz", 17: "disèt", 18: "dizuit", 19: "diznèf", 20: "ven",
    21: "venteyen", 22: "vennde", 33: "tranntwa", 41: "karanteyen", 45: "karannsenk",
    46: "karannsis", 70: "swasanndis", 79: "swasanndiznèf", 80: "katreven",
    90: "katrevendis", 99: "katrevendiznèf", 100: "san", 101: "san en", 200: "de san",
    1000: "mil", 1_000_000: "yon milyon", 1_000_000_000: "yon milya",
}


class Numbers(unittest.TestCase):
    def test_source_spellings(self):
        for number, words in FROM_SOURCE.items():
            with self.subTest(number=number):
                self.assertEqual(number_to_words(number), words)

    def test_t_form_before_one_eight_nine(self):
        self.assertEqual(number_to_words(28), "ventuit")
        self.assertEqual(number_to_words(39), "trantnèf")
        self.assertEqual(number_to_words(61), "swasanteyen")

    def test_bigger_numbers(self):
        self.assertEqual(number_to_words(25), "vennsenk")
        self.assertEqual(number_to_words(2026), "de mil vennsis")
        self.assertEqual(number_to_words(2_500_000), "de milyon senk san mil")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            number_to_words(-1)


if __name__ == "__main__":
    unittest.main()

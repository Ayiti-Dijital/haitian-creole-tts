import unittest

from kreyol.g2p import DEFAULT_LEXICON, load_lexicon, text_to_phones, word_to_phones
from kreyol.phones import PAD, PHONES, SYMBOL_TO_ID, SYMBOLS


def phones(word: str) -> str:
    return " ".join(word_to_phones(word))


class SoundRules(unittest.TestCase):
    def test_nasal_vowels(self):
        self.assertEqual(phones("chen"), "ʃ ɛ̃")
        self.assertEqual(phones("pan"), "p ã")
        self.assertEqual(phones("bonbon"), "b ɔ̃ b ɔ̃")
        self.assertEqual(phones("manje"), "m ã ʒ e")

    def test_grave_accent_keeps_the_vowel_oral(self):
        self.assertEqual(phones("chèn"), "ʃ ɛ n")
        self.assertEqual(phones("pàn"), "p a n")
        self.assertEqual(phones("mòn"), "m ɔ n")

    def test_n_before_a_vowel_starts_the_next_syllable(self):
        self.assertEqual(phones("ane"), "a n e")
        self.assertEqual(phones("fenèt"), "f e n ɛ t")
        self.assertEqual(phones("lanne"), "l ã n e")

    def test_double_n_after_a_nasal_vowel(self):
        self.assertEqual(phones("grann"), "ɡ ɣ ã n")
        self.assertEqual(phones("konnen"), "k ɔ̃ n ɛ̃")
        self.assertEqual(phones("bannann"), "b ã n ã n")
        self.assertEqual(phones("anndan"), "ã n d ã")

    def test_in_and_oun_are_oral(self):
        self.assertEqual(phones("machin"), "m a ʃ i n")
        self.assertEqual(phones("moun"), "m u n")
        self.assertEqual(phones("kounye"), "k u n j e")

    def test_ui_and_semivowels(self):
        self.assertEqual(phones("uit"), "ɥ i t")
        self.assertEqual(phones("dizuit"), "d i z ɥ i t")
        self.assertEqual(phones("mwen"), "m w ɛ̃")
        self.assertEqual(phones("anyen"), "ã j ɛ̃")
        self.assertEqual(phones("Ayiti"), "a j i t i")

    def test_consonant_pairs_and_r(self):
        self.assertEqual(phones("djòb"), "d ʒ ɔ b")
        self.assertEqual(phones("tchala"), "t ʃ a l a")
        self.assertEqual(phones("rezon"), "ɣ e z ɔ̃")

    def test_ng_only_in_ing_loanwords(self):
        self.assertEqual(phones("bilding"), "b i l d i ŋ")
        self.assertEqual(phones("lang"), "l ã ɡ")

    def test_foreign_letters_are_guessed_and_reported(self):
        foreign: set[str] = set()
        self.assertEqual(word_to_phones("taxi", foreign=foreign), ["t", "a", "k", "s", "i"])
        self.assertEqual(foreign, {"x"})

    def test_lexicon_wins_over_the_rules(self):
        lexicon = load_lexicon(DEFAULT_LEXICON)
        self.assertEqual(word_to_phones("oungan", lexicon), ["ũ", "ɡ", "ã"])
        self.assertEqual(word_to_phones("moun", lexicon), ["m", "u", "n"])


class Sentences(unittest.TestCase):
    def test_short_pronouns_and_punctuation(self):
        expected = ["m", " ", "a", "p", " ", "m", "ã", "ʒ", "e", "."]
        self.assertEqual(text_to_phones("M ap manje."), expected)
        self.assertEqual(text_to_phones("M'ap manje."), expected)

    def test_numbers_are_spoken(self):
        self.assertEqual(" ".join(text_to_phones("8")), "ɥ i t")

    def test_every_output_is_a_known_phone(self):
        text = ("Pwosesè ki nan òdinatè w la fè plizyè milya batman chak segonn. "
                "Èske òdinatè w la gen yon sèvo vre? Anndan CPU a, gen 8 nwayo!")
        known = set(PHONES) | {" ", ",", ".", "?", "!"}
        self.assertLessEqual(set(text_to_phones(text)), known)


class Symbols(unittest.TestCase):
    def test_ids_are_unique_and_padding_is_zero(self):
        self.assertEqual(len(SYMBOL_TO_ID), len(SYMBOLS))
        self.assertEqual(SYMBOL_TO_ID[PAD], 0)


if __name__ == "__main__":
    unittest.main()

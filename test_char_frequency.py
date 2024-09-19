import unittest
from char_frequency import count_character_frequencies

class TestCharacterFrequency(unittest.TestCase):

    def test_regular_string(self):
        self.assertEqual(count_character_frequencies("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_empty_string(self):
        self.assertEqual(count_character_frequencies(""), {})

    def test_single_character(self):
        self.assertEqual(count_character_frequencies("a"), {'a': 1})

    def test_repeated_characters(self):
        self.assertEqual(count_character_frequencies("aaaa"), {'a': 4})

    def test_mixed_characters(self):
        self.assertEqual(count_character_frequencies("abcabc123"), {'a': 2, 'b': 2, 'c': 2, '1': 1, '2': 1, '3': 1})

    def test_special_characters(self):
        self.assertEqual(count_character_frequencies("!@#!"), {'!': 2, '@': 1, '#': 1})

if __name__ == "__main__":
    unittest.main()

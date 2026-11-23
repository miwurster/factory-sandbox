import unittest

from sandbox.text import capitalize_words, reverse_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")

    def test_keeps_existing_capitals(self):
        self.assertEqual(capitalize_words("NASA rocks"), "NASA Rocks")

    def test_keeps_spacing_between_words(self):
        self.assertEqual(capitalize_words("two  spaces"), "Two  Spaces")

    def test_empty_string_stays_empty(self):
        self.assertEqual(capitalize_words(""), "")


if __name__ == "__main__":
    unittest.main()

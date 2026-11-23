import unittest

from sandbox.text import capitalize_words, reverse_words, word_count


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


class WordCountTest(unittest.TestCase):
    def test_counts_space_separated_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_ignores_leading_and_trailing_whitespace(self):
        self.assertEqual(word_count("  leading and trailing  "), 3)

    def test_splits_on_tabs_and_newlines(self):
        self.assertEqual(word_count("tabs\tand\nnewlines"), 3)

    def test_empty_string_has_no_words(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()

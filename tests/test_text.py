import unittest

from sandbox.text import capitalize_words, reverse_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_keeps_runs_of_whitespace_between_words(self):
        self.assertEqual(reverse_words("one  two\tthree"), "three  two\tone")

    def test_keeps_leading_and_trailing_whitespace_at_the_ends(self):
        self.assertEqual(reverse_words(" \tone two  \n"), " \ttwo one  \n")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


if __name__ == "__main__":
    unittest.main()

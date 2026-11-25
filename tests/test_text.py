import unittest
from unittest.mock import patch

from sandbox.text import capitalize_words, initials, reverse_words, split_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


class SplitWordsTest(unittest.TestCase):
    def test_splits_at_whitespace(self):
        self.assertEqual(split_words("Ada Lovelace"), ["Ada", "Lovelace"])

    def test_splits_at_hyphens_and_runs_of_separators(self):
        self.assertEqual(
            split_words("Jean-Paul  Sartre"), ["Jean", "Paul", "Sartre"]
        )

    def test_separators_only_give_no_words(self):
        self.assertEqual(split_words("  - "), [])

    def test_empty_string_gives_no_words(self):
        self.assertEqual(split_words(""), [])


class InitialsTest(unittest.TestCase):
    def test_first_letter_of_each_word(self):
        self.assertEqual(initials("Ada Lovelace"), "AL")

    def test_uppercases_and_splits_at_hyphens(self):
        self.assertEqual(initials("jean-paul sartre"), "JPS")

    def test_empty_name_gives_empty_initials(self):
        self.assertEqual(initials(""), "")

    def test_finds_the_words_with_split_words(self):
        with patch("sandbox.text.split_words", return_value=["x", "y"]) as split:
            self.assertEqual(initials("anything"), "XY")
        split.assert_called_once_with("anything")


if __name__ == "__main__":
    unittest.main()

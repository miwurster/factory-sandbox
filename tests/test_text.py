import unittest

from sandbox.text import capitalize_words, reverse_words, split_words


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


if __name__ == "__main__":
    unittest.main()

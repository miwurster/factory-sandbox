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
    def test_splits_at_whitespace_and_hyphen_runs_dropping_empty_words(self):
        cases = [
            ("Ada Lovelace", ["Ada", "Lovelace"]),
            ("Jean-Paul  Sartre", ["Jean", "Paul", "Sartre"]),
            ("  - ", []),
            ("", []),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(split_words(text), expected)


if __name__ == "__main__":
    unittest.main()

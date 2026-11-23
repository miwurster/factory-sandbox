import unittest

from sandbox.text import capitalize_words, reverse_words, slugify


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


class SlugifyTest(unittest.TestCase):
    def test_replaces_punctuation_and_spaces_with_one_hyphen(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_runs_and_trims_hyphens(self):
        self.assertEqual(slugify("  Many   spaces  "), "many-spaces")

    def test_keeps_digits(self):
        self.assertEqual(slugify("Python 3.12 Release"), "python-3-12-release")

    def test_empty_string_stays_empty(self):
        self.assertEqual(slugify(""), "")

    def test_drops_non_ascii_letters(self):
        self.assertEqual(slugify("Café Münster"), "caf-m-nster")


if __name__ == "__main__":
    unittest.main()

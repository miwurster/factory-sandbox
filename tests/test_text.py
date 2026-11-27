import unittest

from sandbox.text import capitalize_words, reverse_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_uppercases_first_letter_and_keeps_the_rest_and_spacing(self):
        cases = [
            ("hello big world", "Hello Big World"),
            ("NASA rocks", "NASA Rocks"),
            ("two  spaces", "Two  Spaces"),
            ("", ""),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(capitalize_words(text), expected)


if __name__ == "__main__":
    unittest.main()

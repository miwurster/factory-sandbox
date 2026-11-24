import unittest

from sandbox.text import capitalize_words, is_palindrome, reverse_words


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_empty_string_stays_empty(self):
        self.assertEqual(reverse_words(""), "")


class CapitalizeWordsTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(capitalize_words("hello big world"), "Hello Big World")


class IsPalindromeTest(unittest.TestCase):
    def test_ignores_punctuation_spaces_and_case(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_question_reads_the_same_backwards(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_word_that_differs_backwards_is_not_a_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string_is_a_palindrome(self):
        self.assertTrue(is_palindrome(""))

    def test_fraction_is_ignored_like_punctuation(self):
        self.assertTrue(is_palindrome("½a"))


if __name__ == "__main__":
    unittest.main()

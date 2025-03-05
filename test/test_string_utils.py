import unittest
from utils.string_utils import reverse_string, is_palindrome, count_vowels

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertFalse(is_palindrome('hello'))

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello'), 2)
        self.assertEqual(count_vowels('why'), 0)
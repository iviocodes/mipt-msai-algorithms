import unittest

from assignment_10.task_2 import count_distinct


class Test_Task2(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_distinct(""), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(count_distinct("aaa"), 3)

    def test_all_different_characters(self):
        self.assertEqual(count_distinct("abc"), 6)

    def test_palindrome(self):
        self.assertEqual(count_distinct("aba"), 5)

    def test_with_repetition(self):
        self.assertEqual(count_distinct("ababa"), 9)

    def test_longer_string_small_alphabet(self):
        self.assertEqual(count_distinct("aaaaa"), 5)

    def test_mixed_chars(self):
        self.assertEqual(count_distinct("abca"), 9)

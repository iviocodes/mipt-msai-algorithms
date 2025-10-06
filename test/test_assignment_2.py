import unittest

from assignment_2.task_1 import interval_count


class TestTask2(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(interval_count([1, 3, 5, 7, 9], 2, 6), 2)
        self.assertEqual(interval_count([1, 3, 5, 7, 9], 3, 3), 1)
        self.assertEqual(interval_count([1, 3, 5, 7, 9], 0, 10), 5)
        self.assertEqual(interval_count([1, 3, 5, 7, 9], 4, 4), 0)
        self.assertEqual(interval_count([1, 3, 5, 7, 9], 10, 15), 0)

    def test_duplicates(self):
        self.assertEqual(interval_count([1, 3, 3, 3, 5, 7, 7, 9], 3, 3), 3)
        self.assertEqual(interval_count([1, 3, 3, 3, 5, 7, 7, 9], 7, 7), 2)
        self.assertEqual(interval_count([1, 3, 3, 3, 5, 7, 7, 9], 2, 6), 4)
        self.assertEqual(interval_count([1, 3, 3, 3, 5, 7, 7, 9], 1, 9), 8)

    def test_empty(self):
        self.assertEqual(interval_count([], 1, 5), 0)
        self.assertEqual(interval_count([], 0, 100), 0)

    def test_one_element(self):
        self.assertEqual(interval_count([100], 100, 100), 1)
        self.assertEqual(interval_count([100], 99, 100), 1)
        self.assertEqual(interval_count([100], 101, 200), 0)

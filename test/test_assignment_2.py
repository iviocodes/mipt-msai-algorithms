import unittest

from assignment_2.task_1 import interval_count
from assignment_2.task_2 import analyze_trimpazation
from assignment_2.task_3 import find_minimum_distance


class Test_Task1(unittest.TestCase):
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


class Test_Task2(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(analyze_trimpazation(3, 5, 1), 5)
        self.assertEqual(analyze_trimpazation(5, 10, 7), 29)
        self.assertEqual(analyze_trimpazation(10000000, 10000, 1), 83287854395709985)


class Test_Task3(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_minimum_distance([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(find_minimum_distance([8, 9, 4, 7, 12, 15, 1], 3), 7)
        self.assertEqual(find_minimum_distance([1000000000, 0, 1, 10, 11, 100], 4), 11)

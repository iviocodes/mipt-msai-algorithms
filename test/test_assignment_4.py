import unittest

from assignment_4.task_1 import lis
from assignment_4.task_2 import min_length


class Test_Task1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(lis(3, [1, 3, 4]), 3)
        self.assertEqual(lis(5, [2, 1, 3, 4, 2]), 3)
        self.assertEqual(lis(7, [3, 4, 2, 1, 3, 4, 2]), 3)


class Test_Task2(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(min_length(3, [1, 2, 3]), 2)
        self.assertEqual(min_length(4, [11, 1, 2, 3]), 9)
        self.assertEqual(min_length(5, [0, 2, 10, 1, 12]), 4)

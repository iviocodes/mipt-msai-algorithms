import unittest

from assignment_3.task_1 import is_regular


class Test_Task2(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_regular("[()]"), True)
        self.assertEqual(is_regular("[(){}[]]"), True)
        self.assertEqual(is_regular("{((())"), False)

    def test_empty(self):
        self.assertEqual(is_regular(""), True)

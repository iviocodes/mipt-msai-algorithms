import unittest

from assignment_3.task_1 import is_regular
from assignment_3.task_2 import ERROR, Deque, process_command


class Test_Task1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_regular("[()]"), True)
        self.assertEqual(is_regular("[(){}[]]"), True)
        self.assertEqual(is_regular("{((())"), False)

    def test_empty(self):
        self.assertEqual(is_regular(""), True)


class Test_Task2(unittest.TestCase):
    def test_basic(self):
        requests = [
            ("0", 7),
            ("0", 2),
            ("0", 4),
            ("2", None),
            ("0", 2),
            ("3", None),
            ("3", None),
            ("3", None),
            ("3", None),
        ]
        deque = Deque()
        result = []
        for request in requests:
            process_command(deque, request, result)
        self.assertEqual(result, ["3", "2", "4", "2", "7"])

    def test_pop_empty(self):
        deque = Deque()
        result = []
        process_command(deque, "3", result)
        self.assertEqual(result, [ERROR])

import unittest

from assignment_3.task_1 import is_regular
from assignment_3.task_2 import ERROR, Deque, process_command
from assignment_3.task_3 import ShopQueue


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


class Test_Task3(unittest.TestCase):
    def test_basic(self):
        queue = ShopQueue()
        queue.add_regular(1)
        queue.add_regular(2)
        queue.add_regular(3)
        self.assertEqual(queue.size, 3)

    def test_remove(self):
        queue = ShopQueue()
        queue.add_regular(1)
        queue.add_regular(2)
        queue.add_regular(3)
        removed = queue.remove()
        self.assertEqual(removed, 1)

    def test_certificate(self):
        queue = ShopQueue()
        queue.add_regular(1)
        queue.add_regular(3)
        queue.add_by_certificate(2)
        queue.remove()
        removed_by_cert = queue.remove()
        self.assertEqual(removed_by_cert, 2)

    def test_certificate_2(self):
        queue = ShopQueue()
        queue.add_regular(1)
        queue.add_regular(3)
        queue.add_regular(4)
        queue.add_by_certificate(2)
        queue.remove()
        queue.remove()
        removed_by_cert = queue.remove()
        self.assertEqual(removed_by_cert, 2)

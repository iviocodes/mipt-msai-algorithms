import unittest

from assignment_5.task_1 import knapsack
from assignment_5.task_2 import can_divide


class Test_Task1(unittest.TestCase):
    def test_basic(self):
        W, N = 8, 4
        w_list = [3, 3, 5, 6]
        c_list = [3, 5, 10, 14]
        max_cost, selected = knapsack(W, N, w_list, c_list)
        self.assertEqual(max_cost, 15)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected, [2, 3])
        
    def test_no_objects(self):
        W, N = 1, 1
        w_list = [10]
        c_list = [10]
        max_cost, selected = knapsack(W, N, w_list, c_list)
        self.assertEqual(max_cost, 0)
        self.assertEqual(len(selected), 0)
        self.assertEqual(selected, [])
        
        
class Test_Task2(unittest.TestCase):
    def test_basic_yes(self):
        N = 3
        costs = [3, 2, 5]
        self.assertEqual(can_divide(N, costs), True)
        
    def test_basic_no(self):
        N = 4
        costs = [7, 1, 5, 2]
        self.assertEqual(can_divide(N, costs), False)
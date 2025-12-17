import unittest

from assignment_8.task_1 import find_shortest_path
from assignment_8.task_2 import bfs_min_cost


class Test_Task1(unittest.TestCase):
    def test_direct_edge(self):
        # 0 --5-- 1
        n = 2
        m = 1
        s, h = 0, 1
        edges = [(0, 1, 5)]
        dist, path = find_shortest_path(n, m, s, h, edges)
        self.assertEqual(dist, 5)
        self.assertEqual(path, [0, 1])

    def test_two_edges_path(self):
        # 0 --2-- 1 --3-- 2
        n = 3
        m = 2
        s, h = 0, 2
        edges = [(0, 1, 2), (1, 2, 3)]
        dist, path = find_shortest_path(n, m, s, h, edges)
        self.assertEqual(dist, 5)
        self.assertEqual(path, [0, 1, 2])

    def test_choose_cheapest_path(self):
        # 0 --10-- 2
        #  \       ^
        #   1--1---/
        n = 3
        m = 3
        s, h = 0, 2
        edges = [
            (0, 2, 10),
            (0, 1, 1),
            (1, 2, 1),
        ]
        dist, path = find_shortest_path(n, m, s, h, edges)
        self.assertEqual(dist, 2)
        self.assertEqual(path, [0, 1, 2])

    def test_unreachable(self):
        # 0--1, 2 isolated
        n = 3
        m = 1
        s, h = 0, 2
        edges = [(0, 1, 4)]
        dist, path = find_shortest_path(n, m, s, h, edges)
        self.assertEqual(dist, -1)
        self.assertEqual(path, [])


class Test_Task2(unittest.TestCase):
    def test_direct_edge_one_step(self):
        # 0 -> 1 with weight 5, k >= 1
        n, s, f, k = 2, 0, 1, 3
        matrix = [
            [-1, 5],
            [5, -1],
        ]
        ans = bfs_min_cost(n, s, f, k, matrix)
        self.assertEqual(ans, 5)
    
    def test_two_steps_cheaper_than_direct(self):
        # 0 -> 2 (10) and  0 -> 1 -> 2 (2 + 3 = 5)
        n, s, f, k = 3, 0, 2, 3
        matrix = [
            [-1, 2, 10],
            [2, -1, 3],
            [10, 3, -1],
        ]
        ans = bfs_min_cost(n, s, f, k, matrix)
        self.assertEqual(ans, 5)
        
    def test_not_enough_steps(self):
        n, s, f, k = 3, 0, 2, 1
        matrix = [
            [-1, 1, -1],
            [1, -1, 1],
            [-1, 1, -1],
        ]
        ans = bfs_min_cost(n, s, f, k, matrix)
        self.assertEqual(ans, -1)
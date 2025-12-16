import unittest

from assignment_7.task_1 import build_graph, dfs
from assignment_7.task_2 import bfs_shortest_path, find_points


def make_grid(lines):
    return [list(row) for row in lines]


class Test_Task1(unittest.TestCase):
    def test_build_graph_simple(self):
        n = 3
        edges = [(0, 1), (1, 2)]
        graph = build_graph(n, edges)
        expected = [
            [1],
            [0, 2],
            [1],
        ]
        self.assertEqual(graph, expected)

    def test_build_graph_is_undirected(self):
        n = 2
        edges = [(0, 1)]
        graph = build_graph(n, edges)
        self.assertIn(1, graph[0])
        self.assertIn(0, graph[1])

    def test_dfs_collects_component(self):
        graph = [
            [1],  # 0
            [0, 2],  # 1
            [1],  # 2
            [4],  # 3
            [3],  # 4
        ]
        used = [False] * len(graph)
        component = []
        dfs(0, graph, used, component)
        self.assertEqual(sorted(component), [0, 1, 2])
        self.assertFalse(used[3])
        self.assertFalse(used[4])


class Test_Task2(unittest.TestCase):
    def test_find_points_simple(self):
        grid = make_grid(
            [
                "E.#",
                ".X.",
                "###",
            ]
        )
        start, end = find_points(grid)
        self.assertEqual(start, (0, 0))
        self.assertEqual(end, (1, 1))

    def test_shortest_path_sample_1(self):
        grid = make_grid(
            [
                "E.",
                ".X",
            ]
        )
        n, m = 2, 2
        start, end = find_points(grid)
        dist = bfs_shortest_path(n, m, grid, start, end)
        self.assertEqual(dist, 2)

    def test_shortest_path_longer_route(self):
        grid = make_grid(
            [
                "E.#..",
                ".#.#.",
                ".#.#X",
                ".#...",
                ".....",
            ]
        )
        n, m = 5, 5
        start, end = find_points(grid)
        dist = bfs_shortest_path(n, m, grid, start, end)
        self.assertEqual(dist, 10)

import unittest

from assignment_9.task_1 import RMQSegmentTree
from assignment_9.task_2 import RSQFenwick


class Test_Task1(unittest.TestCase):
    def test_build_and_simple_query(self):
        arr = [5, 2, 7, 9]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(0, 4), 2)
        self.assertEqual(st.rmq(1, 3), 2)
        self.assertEqual(st.rmq(2, 4), 7)

    def test_single_element_array(self):
        arr = [42]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(0, 1), 42)
        st.update(0, -5)
        self.assertEqual(st.rmq(0, 1), -5)

    def test_queries_on_padded_part(self):
        arr = [3, 1, 4]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(0, 3), 1)
        self.assertEqual(st.rmq(1, 3), 1)
        self.assertEqual(st.rmq(2, 3), 4)

    def test_update_changes_minimum(self):
        arr = [5, 2, 7, 9]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(0, 4), 2)
        st.update(0, 1)
        self.assertEqual(st.rmq(0, 4), 1)
        self.assertEqual(st.rmq(1, 4), 2)

    def test_multiple_updates(self):
        arr = [8, 6, 7, 5, 3, 0, 9]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(0, 7), 0)

        st.update(5, 10)  # подняли минимум
        self.assertEqual(st.rmq(0, 7), 3)

        st.update(4, -1)  # новый минимум
        self.assertEqual(st.rmq(0, 7), -1)
        self.assertEqual(st.rmq(4, 6), -1)  # локально тоже -1

    def test_rmq_empty_range_like(self):
        arr = [1, 2, 3]
        st = RMQSegmentTree(arr)
        self.assertEqual(st.rmq(1, 1), RMQSegmentTree.INF)


class Test_Task2(unittest.TestCase):
    def test_single_update_and_query(self):
        tree = RSQFenwick(5)
        tree.update(1, 1)
        tree.update(3, 1)
        self.assertEqual(tree.rsq(0, 5), 2)
        self.assertEqual(tree.rsq(0, 2), 1)
        self.assertEqual(tree.rsq(2, 4), 1)
        self.assertEqual(tree.rsq(4, 5), 0)

    def test_prefix_query_equivalence(self):
        tree = RSQFenwick(4)
        for i in [0, 1, 3]:
            tree.update(i, 1)
        for r in range(1, 5):
            self.assertEqual(tree.rsq(0, r), tree.query(r - 1))

    def test_increment_and_decrement(self):
        tree = RSQFenwick(3)
        tree.update(0, 1)
        tree.update(1, 1)
        self.assertEqual(tree.rsq(0, 3), 2)
        tree.update(1, -1)
        self.assertEqual(tree.rsq(0, 3), 1)
        self.assertEqual(tree.rsq(1, 2), 0)
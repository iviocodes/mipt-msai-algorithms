import unittest

from assignment_6.task_1 import MaxHeap


class Test_Task1(unittest.TestCase):
    def test_basic(self):
        heap = MaxHeap()

        heap.push(10, 0, 1)
        heap.push(5, 1, 2)
        heap.push(15, 2, 3)

        _, _, id = heap.pop()
        self.assertEqual(id, 3)

        _, _, id = heap.pop()
        self.assertEqual(id, 1)

        _, _, id = heap.pop()
        self.assertEqual(id, 2)
        
    def test_equal_priority(self):
        heap = MaxHeap()
        
        heap.push(10, 0, 1)
        heap.push(10, 1, 2)
        heap.push(10, 2, 3)
        
        self.assertEqual(heap.pop()[2], 1)
        self.assertEqual(heap.pop()[2], 2)
        self.assertEqual(heap.pop()[2], 3)
        
    def test_mixed_priorities(self):
        heap = MaxHeap()
        
        heap.push(5, 0, 1)
        heap.push(20, 1, 2)
        heap.push(10, 2, 3)
        heap.push(15, 3, 4)
        
        self.assertEqual(heap.pop()[2], 2)
        self.assertEqual(heap.pop()[2], 4)
        self.assertEqual(heap.pop()[2], 3)
        self.assertEqual(heap.pop()[2], 1)

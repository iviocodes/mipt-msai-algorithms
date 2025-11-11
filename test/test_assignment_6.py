import unittest

from assignment_6.task_1 import MaxHeap
from assignment_6.task_2 import kmp


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
        
class Test_Task2(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(kmp("abcde", "eabcd"), 1)
        self.assertEqual(kmp("abcde", "abcda"), -1)
        self.assertEqual(kmp("abcdefgh", "fghabcde"), 3)
        
    def test_no_shift(self):
        self.assertEqual(kmp("abcde", "abcde"), 0)
        self.assertEqual(kmp("a", "a"), 0)
        self.assertEqual(kmp("hello", "hello"), 0)
    
    def test_single_character(self):
        self.assertEqual(kmp("a", "a"), 0)
        self.assertEqual(kmp("a", "b"), -1)
    
    def test_different_lengths(self):
        self.assertEqual(kmp("abc", "abcd"), -1)
        self.assertEqual(kmp("abcd", "abc"), -1)
        self.assertEqual(kmp("", "a"), -1)
        self.assertEqual(kmp("a", ""), -1)
    
    def test_full_cycle(self):
        self.assertEqual(kmp("abc", "cab"), 1)
        self.assertEqual(kmp("abc", "bca"), 2)
        self.assertEqual(kmp("abcd", "dabc"), 1)
        self.assertEqual(kmp("abcd", "cdab"), 2)
        self.assertEqual(kmp("abcd", "bcda"), 3)
    
    def test_no_match(self):
        self.assertEqual(kmp("abc", "xyz"), -1)
        self.assertEqual(kmp("hello", "world"), -1)
        self.assertEqual(kmp("abc", "abd"), -1)

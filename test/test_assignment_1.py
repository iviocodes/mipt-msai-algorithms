import unittest

from assignment_1.task_1 import Student, insertion_sort
from assignment_1.task_2 import partition, qsort
from assignment_1.task_3_built_in_sort import Bunch, choose_bunches


class Test_Task1(unittest.TestCase):
    def test_student_comparison(self):
        student1 = Student(1, 90, "Alice")
        student2 = Student(2, 85, "Bob")
        student3 = Student(3, 90, "Charlie")
        self.assertTrue(student1 < student2)
        self.assertTrue(student1 < student3)
        self.assertFalse(student3 < student1)

    def test_insertion_sort(self):
        students = [
            Student(1, 85, "Alice"),
            Student(2, 90, "Bob"),
            Student(3, 80, "Charlie"),
            Student(4, 90, "David"),
        ]
        insertion_sort(students)
        self.assertEqual(students[0].name, "Bob")  # 90, id=2
        self.assertEqual(students[1].name, "David")  # 90, id=4
        self.assertEqual(students[2].name, "Alice")  # 85
        self.assertEqual(students[3].name, "Charlie")  # 80


class Test_Task2(unittest.TestCase):
    def test_partition_basic(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        pivot = 4
        il, ir = partition(arr, 0, len(arr), pivot)
        self.assertTrue(all(x < pivot for x in arr[0:il]))
        self.assertTrue(all(x == pivot for x in arr[il:ir]))
        self.assertTrue(all(x > pivot for x in arr[ir : len(arr)]))

    def test_qsort_random(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        qsort(arr)
        self.assertEqual(arr, sorted(arr.copy()))

    def test_qsort_duplicates(self):
        arr = [5, 2, 5, 1, 5, 3, 5]
        qsort(arr)
        self.assertEqual(arr, sorted(arr.copy()))


class Test_Task3(unittest.TestCase):
    def test_zero_weight_bunches(self):
        bunches = [Bunch(100, 0), Bunch(50, 0)]
        result = choose_bunches(bunches, 10)
        self.assertEqual(result, 150)

    def test_take_whole_bunches(self):
        bunches = [Bunch(100, 5), Bunch(50, 3)]
        result = choose_bunches(bunches, 10)
        self.assertEqual(result, 150)

    def test_take_fractional_bunch(self):
        bunches = [Bunch(100, 5)]  # 20
        result = choose_bunches(bunches, 3)
        self.assertEqual(result, 60)  # 3 * 20

    def test_mixed_whole_and_fractional(self):
        bunches = [
            Bunch(100, 5),  # 20
            Bunch(60, 3),  # 20
            Bunch(40, 2),  # 20
        ]
        result = choose_bunches(bunches, 7)
        self.assertEqual(result, 140)  # 100 + 40 (2/3 of 60)

    def test_single_bunch_fractional(self):
        bunch = [Bunch(75, 5)]  # 15
        result = choose_bunches(bunch, 3)
        self.assertEqual(result, 45)  # 3 * 15

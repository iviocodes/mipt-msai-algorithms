class Student:
    def __init__(self, id, score, name):
        self.id = id
        self.score = score
        self.name = name

    def __lt__(self, other):
        return (self.score, -self.id) > (other.score, -other.id)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    students = []
    students_count = int(input())
    for _ in range(students_count):
        data = input().split()
        students.append(Student(int(data[0]), int(data[1]), data[2]))

    insertion_sort(students)
    for i in range(3):
        print(students[i].name)

    print(" ".join([str(student.id) for student in students]))

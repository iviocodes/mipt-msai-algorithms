import random


class Bunch:
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight

    def __lt__(self, other):
        return (self.cost * other.weight) < (other.cost * self.weight)


def partition(arr, left, right, pivot):
    less = left
    equal = left
    current = left

    while current < right:
        if arr[current] > pivot:
            arr[current], arr[less] = arr[less], arr[current]
            if less < equal:
                arr[current], arr[equal] = arr[equal], arr[current]
            less += 1
            equal += 1
            current += 1
        elif arr[current] == pivot:
            arr[current], arr[equal] = arr[equal], arr[current]
            equal += 1
            current += 1
        else:
            current += 1

    return less, equal


def qsort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    if right - left > 1:
        pivot = arr[random.randint(left, right - 1)]
        less, equal = partition(arr, left, right, pivot)
        qsort(arr, left, less)
        qsort(arr, equal, right)


def choose_bunches(bunches, capacity):
    total_cost = 0
    remaining_capacity = capacity

    for bunch in bunches:
        if remaining_capacity <= 0:
            break

        if bunch.weight == 0:
            total_cost += bunch.cost
            continue

        if bunch.weight <= remaining_capacity:
            total_cost += bunch.cost
            remaining_capacity -= bunch.weight
        else:
            taken_cost = bunch.cost * remaining_capacity // bunch.weight
            total_cost += taken_cost
            remaining_capacity = 0

    return total_cost


if __name__ == '__main__':
    bunches_number, capacity = map(int, input().split())
    bunches_with_weight = []
    bunches = []

    for _ in range(bunches_number):
        cost, weight = map(int, input().split())
        if weight == 0:
            bunches.append(Bunch(cost, weight))
        else:
            bunches_with_weight.append(Bunch(cost, weight))

    qsort(bunches_with_weight)
    bunches.extend(bunches_with_weight)
    print(choose_bunches(bunches, capacity))

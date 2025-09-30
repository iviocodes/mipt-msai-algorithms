class Bunch:
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight


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
            taken_cost = (bunch.cost * remaining_capacity) // bunch.weight
            total_cost += taken_cost
            remaining_capacity = 0

    return total_cost


if __name__ == '__main__':
    bunches_number, capacity = map(int, input().split())
    bunches_with_weight = []
    bunches = []

    for _ in range(bunches_number):
        cost, weight = map(int, input().split())
        if cost <= 0 or weight < 0:
            continue

        if weight == 0:
            bunches.append(Bunch(cost, weight))
        else:
            bunches_with_weight.append(Bunch(cost, weight))

    bunches_with_weight.sort(
        key=lambda bunch: bunch.cost / bunch.weight,
        reverse=True,
    )

    bunches.extend(bunches_with_weight)

    print(choose_bunches(bunches, capacity))

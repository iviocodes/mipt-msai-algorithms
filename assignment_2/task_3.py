def can_place(arr, m, dist):
    count = 1
    last_position = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - last_position >= dist:
            count += 1
            last_position = arr[i]
            if count >= m:
                return True
    return count >= m


def bi_search(arr, m):
    left = 0
    right = arr[-1] - arr[0]
    res = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place(arr, m, mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res


def find_minimum_distance(arr, m):
    arr.sort()
    return bi_search(arr, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    places = list(map(int, input().split()))
    print(find_minimum_distance(places, m))

def bi_search_left(arr, l):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < l:
            left = mid + 1
        else:
            right = mid
    return left


def bi_search_right(arr, r):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= r:
            left = mid + 1
        else:
            right = mid
    return left


def interval_count(scores, l, r):
    # scores.sort()
    left = bi_search_left(scores, l)
    right = bi_search_right(scores, r)
    return right - left


if __name__ == "__main__":
    n, m = map(int, input().split())
    scores = list(map(int, input().split()))
    ranges = [tuple(map(int, input().split())) for _ in range(m)]
    scores.sort()
    for l, r in ranges:
        print(interval_count(scores, l, r))

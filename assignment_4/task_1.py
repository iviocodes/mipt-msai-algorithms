import bisect


def lis(n, x):
    if n == 0:
        return 0

    INF = 10**9
    d = [INF] * (n + 1)
    d[0] = -INF

    for i in range(n):
        pos = bisect.bisect_left(d, x[i])
        d[pos] = x[i]

    k = n
    while k > 0 and d[k] == INF:
        k -= 1

    return k


if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    print(lis(n, x))

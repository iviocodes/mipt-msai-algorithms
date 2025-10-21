def min_length(n, coordinates):
    coordinates.sort()

    dp = [0] * n
    dp[0] = float("inf")
    dp[1] = coordinates[1] - coordinates[0]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + (coordinates[i] - coordinates[i - 1])
    return dp[n - 1]


if __name__ == "__main__":
    n = int(input())
    coordinates = list(map(int, input().split()))
    print(min_length(n, coordinates))

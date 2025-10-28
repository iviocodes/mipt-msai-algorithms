def can_divide(N, costs):
    total_sum = sum(costs)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for cost in costs:
        for j in range(target, cost - 1, -1):
            if dp[j - cost]:
                dp[j] = True

    return True if dp[target] else False


if __name__ == "__main__":
    N = int(input())
    costs = list(map(int, input().split()))
    print("YES" if can_divide(N, costs) else "NO")

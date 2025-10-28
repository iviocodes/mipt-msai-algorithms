def knapsack(W, N, w_list, c_list):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w_list[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_list[i - 1]] + c_list[i - 1])

    max_cost = dp[N][W]
    selected = []
    current_w = W

    for i in range(N, 0, -1):
        if dp[i][current_w] != dp[i - 1][current_w]:
            selected.append(i)
            current_w -= w_list[i - 1]

    selected.reverse()
    return (max_cost, selected)


if __name__ == "__main__":
    (W, N) = map(int, input().split())
    w_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    (max_cost, selected) = knapsack(W, N, w_list, c_list)
    print(max_cost)
    print(len(selected))
    if selected:
        print(" ".join(map(str, selected)))
    else:
        print()

from collections import deque


def bfs_min_cost(n, s, f, k, matrix):
    INF = float("inf")
    min_cost = [[INF] * (k + 2) for _ in range(n)]
    min_cost[s][0] = 0

    queue = deque()
    queue.append((s, 0, 0))

    while queue:
        u, cost, steps = queue.popleft()

        if steps == k:
            continue

        for v in range(n):
            if matrix[u][v] != -1:
                new_cost = cost + matrix[u][v]
                if new_cost < min_cost[v][steps + 1]:
                    min_cost[v][steps + 1] = new_cost
                    queue.append((v, new_cost, steps + 1))

    ans = min(min_cost[f][1 : k + 1])
    return ans if ans < INF else -1

if __name__ == "__main__":
    n, s, f, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(bfs_min_cost(n, s, f, k, matrix))

import heapq
from collections import defaultdict


def find_shortest_path(n, m, s, h, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float("inf")] * n
    parent = [-1] * n
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[h] == float("inf"):
        return -1, []

    path = []
    current = h
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return int(dist[h]), path


if __name__ == "__main__":
    n, m = map(int, input().split())
    s, h = map(int, input().split())

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    weight, path = find_shortest_path(n, m, s, h, edges)

    print(weight)
    if weight != -1:
        print(len(path))
        print(" ".join(map(str, path)))

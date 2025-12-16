import sys

sys.setrecursionlimit(10**7)


def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        v, u = map(int, input().split())
        edges.append((v, u))
    return n, edges


def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)
    return graph


def dfs(start, graph, used, component):
    used[start] = True
    component.append(start)
    for to in graph[start]:
        if not used[to]:
            dfs(to, graph, used, component)


def find_components(graph):
    n = len(graph)
    used = [False] * n
    components = []
    for v in range(n):
        if not used[v]:
            comp = []
            dfs(v, graph, used, comp)
            components.append(comp)
    return components


if __name__ == "__main__":
    n, edges = read_input()
    graph = build_graph(n, edges)
    components = find_components(graph)
    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))

from collections import deque


def read_input():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(str, input())))
    return n, m, grid


def find_points(grid):
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == "E":
                start = (i, j)
            elif ch == "X":
                end = (i, j)
    return start, end


def bfs_shortest_path(n, m, grid, start, end):
    IMP = -1
    if not start or not end:
        return IMP

    q = deque()
    dist = [[IMP] * m for _ in range(n)]

    sx, sy = start
    q.append((sx, sy))
    dist[sx][sy] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return dist[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] != "#" and dist[nx][ny] == IMP:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return IMP


if __name__ == "__main__":
    n, m, grid = read_input()
    start, end = find_points(grid)
    ans = bfs_shortest_path(n, m, grid, start, end)
    print(ans)

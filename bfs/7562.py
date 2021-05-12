from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    sx, sy = map(int, stdin.readline().split())
    ex, ey = map(int, stdin.readline().split())
    visited = [[0 for _ in range(N)] for _ in range(N)]

    q = deque([(sx, sy)])
    visited[sx][sy] = 1

    while len(q):
        x, y = q.popleft()

        if x == ex and y == ey:
            print(visited[ex][ey] - 1)
            break

        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                continue
            if visited[nx][ny] > 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
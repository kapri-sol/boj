from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

field = []
visited = [[0 for _ in range(M)] for _ in range(N) ]

for _ in range(N):
    word = stdin.readline()

    line = []

    for char in word[:-1]:
        line.append(int(char))

    field.append(line)

q = deque([(0, 0)])
visited[0][0] = 1

while len(q):
    x, y = q.popleft()

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
            continue
        if field[nx][ny] == 0 or visited[nx][ny] > 0:
            continue
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1

print(visited[N-1][M-1])
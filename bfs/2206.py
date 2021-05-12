from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

field = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    field.append(list(map(int, stdin.readline()[:-1])))

q = deque([(0, 0)])
visited[0][0] = 1

while len(q):
    x, y = q.pop()

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > N
            
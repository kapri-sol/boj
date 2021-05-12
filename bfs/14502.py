from sys import stdin
from collections import deque
import copy

N, M = map(int, stdin.readline().split())

field = []
safety = []
v = []
maxCnt = 0

for _ in range(N):
    field.append(list(map(int, stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            safety.append((i, j))
        if field[i][j] == 2:
            v.append((i, j))

def bfs():
    virus = deque(v)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    tmpField = copy.deepcopy(field)

    for vx, vy in v:
        visited[vx][vy] = 1   
    while len(virus):
        x, y = virus.popleft()
        tmpField[x][y] = 2

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if tmpField[nx][ny] != 0 or visited[nx][ny] == 1:
                continue

            virus.append((nx, ny))
            visited[nx][ny] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmpField[i][j] == 0:
                cnt += 1
    global maxCnt
    maxCnt = max(maxCnt, cnt)

def createWall(idx, cnt):
    if cnt == 3:
        bfs()
        return

    if idx == len(safety):
        return

    x, y = safety[idx]

    field[x][y] = 1
    createWall(idx + 1, cnt + 1)
    field[x][y] = 0
    createWall(idx + 1, cnt)

createWall(0, 0)

print(maxCnt)
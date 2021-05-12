import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(x, y):

    visited[x][y] = 1

    _x = [-1, 0, 1, 0]
    _y = [0, -1, 0, 1]

    for i in range(4):
        visitX = x + _x[i]
        visitY = y + _y[i]

        if visitX < 0 or visitY < 0 or visitX > N - 1 or visitY > M - 1:
            continue
        if field[visitX][visitY] == 0 or visited[visitX][visitY] == 1:
            continue
        
        dfs(visitX, visitY)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    field = [[0 for _ in range(M)] for __ in range(N)]

    for _ in range(K):
        Y, X  = map(int, sys.stdin.readline().split())
        field[X][Y] = 1

    visited = [[0 for _ in range(M)] for __ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)

    print(cnt)
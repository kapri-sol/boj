from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(r, c):
    visited[r][c] = 1

    _r = [-1, 0, 1, 0]
    _c = [0, -1, 0, 1]

    cnt = 1

    for i in range(4):
        visitR = r + _r[i]
        visitC = c + _c[i]

        if visitR < 0 or visitC < 0 or visitR > N - 1 or visitC > M - 1:
            continue
        if field[visitR][visitC] == 0 or visited[visitR][visitC] == 1:
            continue

        cnt += dfs(visitR, visitC)

    return cnt

N, M, K = map(int, stdin.readline().split())

field = [[0 for _ in range(M)] for __ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]

for _ in range(K):
    r, c = map(int, stdin.readline().split())
    field[r-1][c-1] = 1

MAX = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 1 and visited[i][j] == 0:
            trash = dfs(i, j)

            if trash > MAX:
                MAX = trash

print(MAX)
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(i, j):
    visited[i][j] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx < 0 or ny < 0 or nx > N -1 or ny > N -1:
            continue
        if field[nx][ny] <= height or visited[nx][ny] == 1:
            continue

        dfs(nx, ny)
    
N = int(stdin.readline())

field = []

MIN_HEIGHT = 101
MAX_HEIGHT = 0

maxWaterCnt = 0
maxHeight = -1

for i in range(N):
    heights = list(map(int, stdin.readline().split()))
    minHeight = min(heights)
    maxHeight = max(heights)
    
    
    if minHeight < MIN_HEIGHT:
        MIN_HEIGHT = minHeight
    if maxHeight > MAX_HEIGHT:
        MAX_HEIGHT = maxHeight

    field.append(heights)

maxSafeArea = 0

for height in range(MIN_HEIGHT -1, MAX_HEIGHT + 1):
    visited = [[0 for _ in range(N)] for __ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] > height and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)

    if cnt > maxSafeArea:
        maxSafeArea = cnt    

print(maxSafeArea)
    

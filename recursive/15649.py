import sys

N, M = map(int, sys.stdin.readline().split())

arr = []
visited = [False] * N

def comb(depth):
    if depth == M:
        print(' '.join(arr))
        return
    
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            arr.append(str(i + 1))
            comb(depth + 1)
            arr.pop()
            visited[i] = False

comb(0)
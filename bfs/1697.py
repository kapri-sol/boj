from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

visited = [0 for _ in range(100001)]

q = deque([N])
visited[N] = 1

while len(q):
    x = q.popleft()

    if x == K:
        print(visited[x] - 1)
        break

    for nx in [x - 1, x + 1, x * 2]:
        if nx < 0 or nx > 100000:
            continue
        if visited[nx] > 0:
            continue

        q.append(nx)
        visited[nx] = visited[x] + 1
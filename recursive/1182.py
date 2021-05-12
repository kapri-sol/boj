import sys

N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

seq = []

cnt = 0

def comb(idx):
    global cnt
    if idx == N:
        if len(seq) and sum(seq) == S:
            cnt += 1
        return
    
    seq.append(arr[idx])
    comb(idx + 1)
    seq.pop()

    comb(idx + 1)

comb(0)

print(cnt)
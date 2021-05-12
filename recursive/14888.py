import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
OP = list(map(int, sys.stdin.readline().split()))

MAX = -100000000
MIN = 100000000

def calculate(idx, result, plus, minus, mul, div):
    if idx == N - 1:
        global MAX
        global MIN
        if result > MAX:
            MAX = result
        if result < MIN:
            MIN = result
        return
    
    if plus:
        calculate(idx + 1, result + A[idx + 1], plus - 1, minus, mul, div)
    if minus:
        calculate(idx + 1, result - A[idx + 1], plus, minus - 1, mul, div)
    if mul:
        calculate(idx + 1, result * A[idx + 1], plus, minus, mul - 1, div)
    if div:
        calculate(idx + 1, -(-result // A[idx + 1]) if result < 0 else result // A[idx + 1], plus, minus, mul, div - 1)

calculate(0, A[0], OP[0], OP[1], OP[2], OP[3])

print(MAX)
print(MIN)
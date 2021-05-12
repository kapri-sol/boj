import sys

word = sys.stdin.readline()[:-1]

def checkF(left, right):
    if left >= right:
        return 1
    
    if word[left] != word[right]:
        return 0
    else:
        return checkF(left + 1, right - 1)

print(checkF(0, len(word) - 1))
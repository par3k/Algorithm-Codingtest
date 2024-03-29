# N과 M(3)
import sys

n, m = map(int, sys.stdin.readline().split())

ans = [0] * (n + 1)

def recursive(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        ans[depth] = i
        recursive(depth + 1)

recursive(0)
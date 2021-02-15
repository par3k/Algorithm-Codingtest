# 로또
import sys

def dfs(start, depth):
    if depth == 6:
        print(' '.join(map(str, visited)))
        return

    for i in range(start, len(arr)):
        visited[depth] = arr[i]
        dfs(i+1, depth+1)


while True:
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    if data[0] == 0: break

    arr = data[1:]
    visited = [0] * 6

    dfs(0, 0)
    print()


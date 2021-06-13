# 순열 사이클
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000001)


def dfs(i):
    visited[i] = 1
    a = arr[i]
    if not visited[a]:
        dfs(a)


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    ans = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)
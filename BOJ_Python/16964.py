# DFS 스페셜 저지
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000001)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
ans = list(map(int, input().split()))
level = [False] * (n + 1)
tsize = [0] * (n + 1)


def dfs(n, lv):
    if visited[n]: return 0
    visited[n] = True
    size = 1
    level[n] = lv
    for i in range(len(graph[n])):
        next = graph[n][i]
        size += dfs(next, lv + 1)
    tsize[n] = size
    return size

if ans[0] != 1:
    print("0")
    sys.exit(0)
else:
    dfs(1, 0)
    for i in range(1, n):
        x = ans[i]
        if tsize[x] == 1 or i + tsize[x] >= n:
            continue
        next = ans[i + tsize[x]]
        if level[next] > level[x]:
            print(0)
            sys.exit(0)
    print(1)

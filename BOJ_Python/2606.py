# 바이러스
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
w = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(w):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    graph[to_].append(from_)
cnt = 0

def dfs(node):
    global cnt
    visited[node] = 1
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt


print(dfs(1))
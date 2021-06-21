# 트리
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
node = list(map(int, input().split()))
delete_node = int(input())

graph = [[0] * n for _ in range(n)]
visited = [0] * n
cnt = 0

for i in range(n):
    if node[i] != -1:
        graph[i][node[i]] = 1
        graph[node[i]][i] = 1
    else:
        root = i

for i in range(n):
    graph[i][delete_node] = 0
    graph[delete_node][i] = 0


def dfs(node):
    global cnt
    switch = 0
    visited[node] = 1
    for i in range(n):
        if not visited[i] and graph[node][i]:
            switch = 1
            dfs(i)
    if not switch:
        cnt += 1


dfs(root)

if delete_node == root:
    print(0)
else:
    print(cnt)
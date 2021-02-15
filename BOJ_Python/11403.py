import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n


def dfs(x, y):
    visited[y] = True
    graph[x][y] = 1

    for i in range(n):
        if not visited[i] and graph[y][i] == 1:
            dfs(x, i)


for i in range(n):
    for j in range(n):
        visited[j] = False

    for j in range(n):
        if graph[i][j] == 1 and not visited[j]:
            dfs(i, j)

for i in range(n):
    print(" ".join(map(str, graph[i])))
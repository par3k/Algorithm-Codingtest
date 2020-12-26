# 맥주 마시면서 걸어가기
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

def make():
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j: continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                graph_[i][j], graph_[j][i] = 1, 1


def dfs(start):
    visited[start] = True
    for i in range(n + 2):
        if graph_[start][i] == 1 and not visited[i]:
            dfs(i)


for _ in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n + 2)]
    graph_ = [[0] * (n + 2) for _ in range(n + 2)]
    visited = [False for _ in range(n + 2)]
    make()
    dfs(0)
    if visited[n + 1]:
        print("happy")
    else:
        print("sad")

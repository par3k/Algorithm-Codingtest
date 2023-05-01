# 점프왕 쩰리(Large)
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [0, 1], [1, 0]

def dfs(x, y):
    visited[x][y] = True
    jump = graph[x][y]
    if graph[x][y] == -1:
        print("HaruHaru")
        exit()
    for i in range(2):
        nx, ny = x + dx[i] * jump, y + dy[i] * jump
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                dfs(nx, ny)

dfs(0, 0)
print("Hing")
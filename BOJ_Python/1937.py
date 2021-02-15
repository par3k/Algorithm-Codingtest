# 욕심쟁이 판다
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y]: return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny <n:
            if graph[nx][ny] > graph[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
# 알파벳 - pypy3로만 해결가능
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
alpha = [0] * 26
ans = 0


def dfs(x, y, m):
    global ans
    ans = max(ans, m)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and alpha[graph[nx][ny]] == 0:
            alpha[graph[nx][ny]] = 1
            dfs(nx, ny, m+1)
            alpha[graph[nx][ny]] = 0


alpha[graph[0][0]] = 1
dfs(0, 0, 1)
print(ans)
# 연구소
import sys
sys.setrecursionlimit(1001)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0] , [0, 0, -1, 1]
ans = 0


def spread_virus(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                spread_virus(nx, ny)


def safe_area():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def dfs(wall):
    global ans
    if wall == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    spread_virus(i, j)

        ans = max(ans, safe_area())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall += 1
                dfs(wall)
                graph[i][j] = 0
                wall -= 1


dfs(0)
print(ans)
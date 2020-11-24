# 치즈
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def cheese_check(n, m):
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                return False
    return True


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] != 0:
                graph[nx][ny] += 1
            else:
                visited[nx][ny] = True
                dfs(nx, ny)


def remove_cheese(graph, n, m):
    for x in range(n):
        for y in range(m):
            if graph[x][y] >= 3:
                graph[x][y] = 0
            elif graph[x][y] > 0:
                graph[x][y] = 1
    return graph


ans = 0
while True:
    visited = [[False] * m for _ in range(n)]
    if cheese_check(n, m):
        print(ans)
        break
    visited[0][0] = True
    dfs(0, 0)
    graph = remove_cheese(graph, n, m)
    ans += 1
# 양치기 꿍
import sys
sys.setrecursionlimit(1000001)
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
wolf, sheep = 0, 0


def eat_dfs(x, y):
    global wolf, sheep
    if graph[x][y] == 'v':
        wolf += 1
    elif graph[x][y] == 'k':
        sheep += 1
    graph[x][y] = '#'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != '#':
                eat_dfs(nx, ny)


result = [0, 0]
for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            sheep, wolf = 0, 0
            eat_dfs(i, j)

            if sheep > wolf:
                result[0] += sheep
            else:
                result[1] += wolf

print(result[0], result[1])
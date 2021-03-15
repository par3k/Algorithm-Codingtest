# 미로 2
import sys
sys.setrecursionlimit()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    global ans
    visited[x][y] = True
    if ans: return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:
            if not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                if graph[nx][ny] == 3:
                    ans = 1
                dfs(nx, ny)


for _ in range(1,11):
    t = int(input())
    graph = list()

    for i in range(100):
        line = list(map(int, list(input().strip())))
        graph.append(line)

    visited = [[False] * 100 for _ in range(100)]
    ans = 0
    dfs(1, 1)
    print(f'#{t} {ans}')
# 단지번호붙이기
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0


def dfs(x, y, num):
    global cnt
    visited[x][y] = 1

    if graph[x][y] == 1:
        cnt += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, num)
                visited[nx][ny] = 1

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, 1)
            arr.append(cnt)
            cnt = 0

print(len(arr))
arr.sort()
for i in arr:
    print(i)
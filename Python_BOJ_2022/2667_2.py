# 단지 번호 붙이기
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

def dfs(x, y):
    global cnt
    visit[x][y] = True
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visit[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

ans = []
for i in range(n):
    for j in range(n):
        if not visit[i][j] and graph[i][j] == 1:
            dfs(i, j)
            ans.append(cnt)
            cnt = 0

print(len(ans))
for i in ans:
    print(i)
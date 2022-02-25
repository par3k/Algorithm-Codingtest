# 단지번호붙이기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = 0
ans = []

def recursive(x, y):
    global cnt
    visited[x][y] = 1
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny <n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                recursive(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            recursive(i, j)
            ans.append(cnt)
            cnt = 0

print(len(ans))
ans.sort()
for i in ans:
    print(i)
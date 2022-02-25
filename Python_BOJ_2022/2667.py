# 단지번호붙이기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# DFS - 재귀를 이용한 풀이
# cnt = 0
# ans = []

# def recursive(x, y):
#     global cnt
#     visited[x][y] = 1
#     if graph[x][y] == 1:
#         cnt += 1
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny <n:
#             if not visited[nx][ny] and graph[nx][ny] == 1:
#                 recursive(nx, ny)


# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1 and not visited[i][j]:
#             recursive(i, j)
#             ans.append(cnt)
#             cnt = 0

# BFS 풀이
from collections import deque

cnt = 0
ans = []

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    if graph[x][y] == 1:
        cnt += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            ans.append(cnt)
            cnt = 0

print(len(ans))
ans.sort()
for i in ans:
    print(i)
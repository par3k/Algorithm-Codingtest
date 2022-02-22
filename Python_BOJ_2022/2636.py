# 치즈
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 전체 치즈 갯수가 몇갠지 맨 처음 카운트
left_cheese = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            left_cheese += 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 치즈 테두리를 너비우선탐색으로 돌며 2로 바꿔준다
def bfs(cheese):
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 2
                        cheese -= 1
                        # print_graph()
                    else:
                        queue.append((nx, ny))
    return cheese

cnt = 0
tmp = left_cheese

# def print_graph():
#     print('===================================================')
#     for i in range(n):
#         for j in range(m):
#             print(graph[i][j], end=' ')
#         print()

# 테두리 부분 치즈를 없앤다.
def remove_cheese():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 0

# 치즈의 갯수가 존재하는 동안 계속 탐색
while left_cheese:
    visited = [[False] * m for _ in range(n)]
    left_cheese = bfs(left_cheese)
    if left_cheese != 0:
        tmp = left_cheese
    cnt += 1
    remove_cheese()

print(cnt)
print(tmp)
# 토마토
from collections import deque

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 토마토가 익는다
def find():
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[xx][yy] + 1
                    queue.append((nx, ny))


# 토마토 존재하는 위치 체크후, 위치를 덱에 저장
queue = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
                queue.append((i, j))

# 토마토를 익혀본다
find()

# 만약 익지 않은 토마토가 있으면 -1 출력
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit()

# 토마토가 전부 익는데 걸리는 시간 확인
ans = -123456789
for i in range(m):
    for j in range(n):
        ans = max(graph[i][j], ans)

print(ans - 1)
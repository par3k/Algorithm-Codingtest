# 마법사 상어와 비바라기
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split()) # graph size, turn
graph = [list(map(int, input().split())) for _ in range(n)]
cmd = [list(map(int, input().split())) for _ in range(m)] # 방향, 이동거리 [[1, 3], [3, 4], [8, 1], [4, 8]]
dx, dy = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1] # dx[0], dy[0]은 무시
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
cloud = deque(cloud) # 맨 처음 구름 위치 (무조건 4개임)

# 구름의 방향과, 이동거리가 제시되면 그만큼 이동된 구름의 위치를 찾는다.
def move_cloud(d, dist):
    global n
    size = len(cloud)
    for _ in range(size):
        x, y = cloud.popleft()
        nx, ny = (x + dx[d] * dist) % n, (y + dy[d] * dist) % n
        # 왼쪽으로 이동할 경우, 위치 보정
        if 0 > nx: nx += n
        if 0 > ny: ny += n
        
        cloud.append((nx, ny))
        visited[nx][ny] = True
        graph[nx][ny] += 1


# 구름이 있는 곳에서 대각선 1의 위치에 물이 있는지 체크하고 있으면 물 복사 버그 발동
def water_magic():
    while cloud:
        x, y = cloud.popleft()
        for i in range(1, 5): # 2, 4, 6, 8
            nx, ny = x + dx[2*i], y + dy[2*i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    graph[x][y] += 1
                

for dir, mov in cmd:
    visited = [[False] * n for _ in range(n)]
    move_cloud(dir, mov)
    water_magic()

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= 2:
                cloud.append((i, j))
                graph[i][j] -= 2

# 답 출력
ans = 0
for i in range(n):
    for j in range(n):
        ans += graph[i][j]

print(ans)
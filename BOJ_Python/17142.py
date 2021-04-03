# 연구소3
from collections import deque
from itertools import combinations
import sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0 , 0, -1, 1]

time = INF


def bfs(virus, min_time, leftArea):
    global time
    queue = deque(virus)
    time_val = 0
    visited = [[False] * n for _ in range(n)]
    for x, y in virus:
        visited[x][y] = True

    while queue:
        if not leftArea:
            break
        time_val += 1
        if time_val >= min_time:
            return INF

        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        if graph[nx][ny] == 0:  leftArea -= 1

    if not leftArea:
        return time_val
    else:
        return INF



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
virusList = list()

left = 0
# 바이러스가 있으면 위치 저장 및 빈 공간 체크
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virusList.append([i, j])
        if graph[i][j] == 0:
            left += 1

# 바이러스 N개 중 m개를 선택 NCm
for virusPosition in combinations(virusList, m):
    time = min(time, bfs(virusPosition, time, left))

# 이동 못 할 경우 -1 출력, 만약 도착 했으면 값을 출력
if time == INF:
    print(-1)
else:
    print(time)

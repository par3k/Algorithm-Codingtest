# 연구소
from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
copy_graph = [[0] * m for _ in range(n)]

# step1. 벽세우기
answer = 0
def build_wall(depth):
    global answer
    if depth == 3:
        for i in range(n):
            for j in range(m):
                copy_graph[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if copy_graph[i][j] == 2:
                    virus_spread(i, j)

        answer = max(answer, count_space())
        return
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                depth += 1
                build_wall(depth)
                graph[i][j] = 0
                depth -= 1


# step2. 바이러스 퍼트리기
def virus_spread(ix, iy):
    virus_map = deque()
    virus_map.append((ix, iy))

    while virus_map:
        x, y = virus_map.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copy_graph[nx][ny] == 0:
                    copy_graph[nx][ny] = 2
                    virus_map.append((nx, ny))

# step3. 빈 공간 세기
def count_space():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                cnt += 1
    return cnt

build_wall(0)
print(answer)
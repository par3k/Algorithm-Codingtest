# 연구소
import sys
from collections import deque
sys.setrecursionlimit(100000)
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp_graph = [[0] * m for _ in range(n)]
ans = 0


def set_wall(wall_cnt): # DFS
    global ans
    if wall_cnt == 3: # 벽 3개 치고
        for i in range(n):
            for j in range(m):
                tmp_graph[i][j] = graph[i][j] # 그래프 복사

        for i in range(n):
            for j in range(m):
                if tmp_graph[i][j] == 2: # 바이러스 있으면
                    virus(i, j) # 바이러스 퍼트리기
        ans = max(ans, countSafe())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall_cnt += 1
                set_wall(wall_cnt)
                graph[i][j] = 0
                wall_cnt -= 1


def virus(x, y): # BFS
    queue = deque()
    queue.append([x, y])
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append([nx, ny])


def countSafe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                cnt += 1
    return cnt


set_wall(0)
print(ans)
# 뱀
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c


dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 상 우 하 좌 CW로 방향 설정


def change(d, c): # 상 우 하 좌로 돌아가야됨
    if c == 'L': # CCW : -1 >> 상 좌 하 우 상
        d = (d - 1) % 4
    else: # CW : +1 >> 상 우 하 좌 상
        d = (d + 1) % 4
    return d


def bfs():
    direction = 1
    time = 1
    x, y = 0, 0

    visited = deque() # 방문 위치
    visited.append([x, y])
    graph[x][y] = 2

    while True:
        x, y = x + dx[direction], y + dy[direction]

        if 0 <= x < n and 0 <= y < n and graph[x][y] != 2:
            if graph[x][y] == 0:  # 사과가 없는 경우
                tmp_x, tmp_y = visited.popleft()
                graph[tmp_x][tmp_y] = 0  # 뱀 꼬리 제거

            graph[x][y] = 2
            visited.append([x, y])

            if time in times.keys():
                direction = change(direction, times[time])
            time += 1

        else:
            return time


print(bfs())


'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
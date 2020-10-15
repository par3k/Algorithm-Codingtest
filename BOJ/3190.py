# # 뱀
from collections import deque

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c


dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 상 우 하 좌


def change(d, c): # 상 우 하 좌로 돌아가야됨
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    dir, time = 1, 1
    x, y = 0, 0
    visited = deque([[x, y]])
    arr[x][y] = 2

    while True:
        x, y = x + dx[dir], y + dy[dir]
        if 0 <= x < n and 0 <= y < n and arr[x][y] != 2:
            if not arr[x][y] == 1:
                tmp_x, tmp_y = visited.popleft()
                arr[tmp_x][tmp_y] = 0

            arr[x][y] = 2
            visited.append([x, y])

            if time in times.keys():
                dir = change(dir, times[time])
            time += 1
        else:
            return time


print(start())
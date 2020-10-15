# # 뱀
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

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


dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0] # 상 우 하 좌 CW로 방향 설정


def change(d, c): # 상 우 하 좌로 돌아가야됨
    # CW : +1 >> 상 우 하 좌 상
    # CCW : -1 >> 상 좌 하 우 상
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    direction = 1
    time = 1
    y, x = 0, 0

    visited = deque([[y, x]])  # 방문 위치
    arr[y][x] = 2

    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < n and 0 <= x < n and arr[y][x] != 2:
            if not arr[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0  # 꼬리 제거

            arr[y][x] = 2
            visited.append([y, x])

            if time in times.keys():
                direction = change(direction, times[time])

            time += 1
        else:
            return time


print(start())
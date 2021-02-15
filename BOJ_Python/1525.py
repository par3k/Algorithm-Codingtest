# 퍼즐
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

graph = [list(map(int, input().split())) for _ in range(3)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    while queue:
        val = queue.popleft()

        if val == 123456789:
            print(distance[val])
            return

        s = str(val)
        k = s.find('9')
        x, y = k // 3, k % 3

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nk = nx * 3 + ny
                ns = list(s)
                ns[k], ns[nk] = ns[nk], ns[k]
                nd = int(''.join(ns))
                if not distance.get(nd):
                    distance[nd] = distance[val] + 1
                    queue.append(nd)

    print(-1)


m = 0
queue, distance = deque(), dict()
for i in range(3):
    for j in range(3):
        n = graph[i][j]
        if not n:
            n = 9
        m = m * 10 + n

queue.append(m)
distance[m] = 0
bfs()
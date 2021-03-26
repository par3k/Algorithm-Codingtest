# 말이 되고픈 원숭이
# 27630824	hoijae0194	 1600	맞았습니다!!	51220	5716	Python 3 / 수정	1296

from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
kx, ky = [2, 1, 2, 1, -2, -1, -2, -1], [1, 2, -1, -2, 1, 2, -1, -2]


def bfs():
    global ans
    queue.append([0, 0, 0, 0])
    visited[0][0][0] = 0
    while queue:
        x, y, k, cnt = queue.popleft()

        if x == h - 1 and y == w - 1:
            ans = visited[x][y][k]
            break
        if k < K:
            for d in range(8):
                nx, ny = x + kx[d], y + ky[d]
                if 0 <= nx < h and 0 <= ny < w:
                    if not visited[nx][ny][k + 1] and graph[nx][ny] == 0:
                        visited[nx][ny][k + 1] = cnt + 1
                        queue.append([nx, ny, k + 1, cnt + 1])

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny][k] and graph[nx][ny] == 0:
                    visited[nx][ny][k] = cnt + 1
                    queue.append([nx, ny, k, cnt + 1])
    return ans


K = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0 for _ in range(K + 1)] for _ in range(w)] for _ in range(h)]

ans = -1
queue = deque()
print(bfs())
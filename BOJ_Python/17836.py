# 공주님을 구해라!
# 27717850	hoijae0194	 17836	맞았습니다!!	32756	120	Python 3 / 수정	971
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
tmp = 123456789


def bfs():
    global tmp
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 2:
            tmp = abs(n - 1 - x) + abs(m - 1 - y) + visited[x][y] - 1
        if x == n - 1 and y == m - 1:
            return min(visited[x][y] - 1, tmp)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
    return tmp


res = bfs()
print("Fail" if(res > t) else res)
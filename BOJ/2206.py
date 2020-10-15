# 벽 부수고 이동하기
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
broke = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    ans = -1
    queue = deque()
    queue.append([x, y, 1, False])
    visited[x][y] = True

    while queue:
        x, y, cnt, destroy = queue.popleft()
        if x == n-1 and y == m-1:
            if ans < 0: ans = cnt
            else: ans = min(cnt, ans)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not destroy:
                    if graph[nx][ny] == 0:
                        if not visited[nx][ny]:
                            queue.append([nx, ny, cnt+1, destroy])
                            visited[nx][ny] = True

                    else:
                        if not broke[nx][ny]:
                            broke[nx][ny] = True
                            queue.append([nx, ny, cnt+1, True])

                else:
                    if graph[nx][ny] == 0:
                        if not broke[nx][ny]:
                            broke[nx][ny] = True
                            queue.append([nx, ny, cnt+1, destroy])
    return ans


print(bfs(0, 0))
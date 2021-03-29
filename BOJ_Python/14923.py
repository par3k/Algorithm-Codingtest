# 미로 탈출
from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfS():
    ans = 0
    queue = deque()
    queue.append((hx, hy, 0))
    visited[0][hx][hy] = True

    while queue:
        ans += 1
        size = len(queue)
        while size > 0:
            x, y, k = queue.popleft()

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1:
                        if k == 0 and not visited[k + 1][nx][ny]:
                            if nx == ex and ny == ey: return ans
                            queue.append((nx, ny, 1))
                            visited[k + 1][nx][ny] = True
                    else:
                        if not visited[k][nx][ny]:
                            if nx == ex and ny == ey: return ans
                            queue.append((nx, ny, k))
                            visited[k][nx][ny] = True
            size -= 1
    return -1


n, m = map(int, input().split())
hx, hy = map(lambda x: int(x) - 1, input().split())
ex, ey = map(lambda x: int(x) - 1, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(2)]
print(bfS())
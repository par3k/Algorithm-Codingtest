# 로봇 청소기
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]   # 북 동 남 서


def move_rotate(a):
    if a == 0:      # 북 > 서
        return 3
    elif a == 1:    # 동 > 북
        return 0
    elif a == 2:    # 남 > 동
        return 1
    elif a == 3:    # 서 > 동
        return 2


def move_back(b):
    if b == 0:      # 북 > 남
        return 2
    elif b == 1:    # 동 > 서
        return 3
    elif b == 2:    # 남 > 북
        return 0
    elif b == 3:    # 서 > 동
        return 1


def bfs(r, c, d):
    ans = 1
    graph[r][c] = 2
    queue = deque([[r, c, d]])

    while queue:
        r, c, d = queue.popleft()
        tmp_d = d

        for i in range(4):
            tmp_d = move_rotate(tmp_d)
            nr, nc = r + dr[tmp_d], c + dc[tmp_d]

            # case : a
            if 0 <= nr < n and 0 <= nc < m and not graph[nr][nc]:
                ans += 1
                graph[nr][nc] = 2
                queue.append([nr, nc, tmp_d])
                break

            elif i == 3:    # case : c
                nr, nc = r + dr[move_back(d)], c + dc[move_back(d)]
                queue.append([nr, nc, d])

                if graph[nr][nc] == 1:  # case : d
                    return ans


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(bfs(r, c, d))




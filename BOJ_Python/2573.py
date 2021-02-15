# 빙산
import sys
from collections import deque, defaultdict
input = lambda : sys.stdin.readline().rstrip()


def bfs(start, maps, visited):
    ice_berg = defaultdict(int)
    queue = deque()
    queue.append(start)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    ice_berg[(x, y)] += 1
                elif maps[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return ice_berg


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def solution(r, c, maps):
    ans = 0
    while True:
        visited = [[0 for _ in range(c)] for _ in range(r)]
        continent = 0

        for x in range(r):
            for y in range(c):
                if maps[x][y] != 0 and not visited[x][y]:
                    ice_berg = bfs((x, y), maps, visited)
                    continent += 1

        if continent > 1:
            return ans
        if continent == 0:
            return 0

        for (x, y), cnt in ice_berg.items():
            maps[x][y] = 0 if maps[x][y] < cnt else maps[x][y] - cnt
        ans += 1


print(solution(n, m, graph))
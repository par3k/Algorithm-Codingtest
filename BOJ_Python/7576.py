# 토마토
import sys
input = lambda : sys.stdin.readline()

N, M = map(int, input().split())

tomato_pos = []
graph = []

for i in range(M):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] == 1:
            tomato_pos.append((i, j))
    graph.append(a)


def bfs(graph, queue):
    cnt = 0
    while queue:
        good = []

        for v in queue:
            x, y = v[0], v[1]

            if y < N-1 and graph[x][y+1] == 0:
                graph[x][y+1] = 1
                good.append((x, y+1))

            if y > 0 and graph[x][y-1] == 0:
                graph[x][y-1] = 1
                good.append((x, y-1))

            if x < M-1 and graph[x+1][y] == 0:
                graph[x+1][y] = 1
                good.append((x+1, y))

            if x > 0 and graph[x-1][y] == 0:
                graph[x-1][y] = 1
                good.append((x-1, y))

        queue = good
        cnt += 1

    for a in graph:
        if a.count(0) != 0:
            return -1

    return cnt - 1


print(bfs(graph, tomato_pos))
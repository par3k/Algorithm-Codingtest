# 플로이드
from heapq import *
import sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)


def dijikstra(start):
    queue = list()
    distance = [INF] * (n + 1)
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cost, current = heappop(queue)
        if distance[current] < cost: continue
        for i in graph[current]:
            cost2 = cost + i[1]
            if distance[i[0]] > cost2:
                distance[i[0]] = cost2
                heappush(queue, (cost2, i[0]))
    return distance


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append([to_, weight])

answer = list()
for i in range(1, n + 1):
    answer.append(dijikstra(i))

for i in range(n):
    for j in range(1, n + 1):
        if answer[i][j] == INF: answer[i][j] = 0
        print(answer[i][j], end=' ')
    print()
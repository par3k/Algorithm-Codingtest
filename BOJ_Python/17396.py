# 백도어
from heapq import *
import sys
input = lambda :sys.stdin.readline().rstrip()


def dijikstra(start):
    queue = list()
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, current = heappop(queue)
        if distance[current] < cost: continue
        for i in graph[current]:
            cost2 = cost + i[1]
            if cost2 < distance[i[0]] and arr[i[0]] == 0:
                distance[i[0]] = cost2
                heappush(queue, (cost2, i[0]))


INF = 1234567890
n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)
arr = list(map(int, input().split()))
arr[-1] = 0

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))
    graph[to_].append((from_, weight))

dijikstra(0)

print(distance[n - 1] if distance[n - 1] != INF else -1)
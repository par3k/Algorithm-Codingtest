# 떡 돌리기  왜 TLE ㅡㅡ
import sys
from heapq import *
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [INF] * n
visited = [False] * n

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append([to_, weight])
    graph[to_].append([from_, weight])


def dijikstra(start):
    queue = list()
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cost, current = heappop(queue)

        if visited[current]: continue
        for i in graph[current]:
            cost2 = cost + i[1]
            if not visited[i[0]] and distance[i[0]] > cost2:
                distance[i[0]] = cost2
                heappush(queue, (cost2, i[0]))
        visited[current] = True


def process():
    dijikstra(y)
    distance.sort()

    if distance[n - 1] * 2 > x:
        print(-1)

    day, idx, tmp = 0, 0, 0
    while idx < n:
        while idx < n and tmp + (distance[idx] * 2) <= x:
            tmp += distance[idx] * 2
            idx += 1

        tmp = 0
        day += 1
    return day


print(process())
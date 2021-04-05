# 백준 1753 최단경로 >> 다익스트라 함수로 파생되는 최단거리 구하는 문제 무조건 풀자
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append([weight, to_])


def dijikstra(start):
    queue = list()
    heapq.heappush(queue, (0, start)) # cost, current
    distance[start] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        if distance[current] < cost: continue
        for i in graph[current]:
            cost2 = cost + i[0]
            if cost2 < distance[i[1]]:
                distance[i[1]] = cost2
                heapq.heappush(queue, (cost2, i[1]))


dijikstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
        
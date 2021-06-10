# 최단 경로
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

v, e = map(int, input().split())
k = int(input())
d = [int(1e9) for _ in range(v + 1)]


def dijikstra(start):
    pq = []
    d[start] = 0
    heapq.heappush(pq, (d[start], start))
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if d[current_node] < current_distance: continue
        for next_node, distance in graph[current_node]:
            if current_distance + distance < d[next_node]:
                d[next_node] = current_distance + distance
                heapq.heappush(pq, (d[next_node], next_node))


graph = [[] for _ in range(v + 1)]
for _ in range(e):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))

dijikstra(k)

for i in d[1:]:
    if i == int(1e9):
        print('INF')
    else:
        print(i)
# 특정한 최단 경로
import sys, heapq

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [int(1e9) for _ in range(v + 1)]

for _ in range(e):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))


def dijikstra(node):
    distance[node] = 0
    heap = []
    heapq.heappush(heap, (distance[node], node))
    while heap:
        c_dist, c_node = heapq.heappop(heap)
        if distance[c_node] < c_dist: continue
        for n_node, n_weight in graph[c_node]:
            if c_dist + n_weight < distance[n_node]:
                distance[n_node] = c_dist + n_weight
                heapq.heappush(heap, (distance[n_node], n_node))


dijikstra(k)
for i in distance[1:]:
    if i == int(1e9):
        print("INF")
    else:
        print(i)
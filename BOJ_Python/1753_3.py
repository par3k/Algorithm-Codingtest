# 최단경로 (다익스트라)
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [int(1e9) for _ in range(v + 1)]

for _ in range(e):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))


def dijikstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (distance[start], start))
    while heap:
        c_distance, c_node = heapq.heappop(heap)
        if distance[c_node] < c_distance: continue
        for n_node, n_distance in graph[c_node]:
            if c_distance + n_distance < distance[n_node]:
                distance[n_node] = c_distance + n_distance
                heapq.heappush(heap, (distance[n_node], n_node))


dijikstra(k)
for i in range(1, len(distance)):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
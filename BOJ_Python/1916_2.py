# 최소비용 구하기
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [int(1e9) for _ in range(n + 1)]

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))

start, end = map(int, input().split())


def dijikstra(start):
    heqp = list()
    heapq.heappush(heqp, (0, start))
    distance[start] = 0
    while heqp:
        c_weight, c_node = heapq.heappop(heqp)
        if distance[c_node] < c_weight:
            continue
        for n_node, n_weight in graph[c_node]:
            if distance[n_node] > c_weight + n_weight:
                distance[n_node] = c_weight + n_weight
                heapq.heappush(heqp, (c_weight + n_weight, n_node))

dijikstra(start)
print(distance[end])
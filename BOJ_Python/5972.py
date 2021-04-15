# 택배 배송
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)


def dijikstra(start):
    queue = list()
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        if distance[current] < cost: continue
        for i in graph[current]:
            cost2 = cost + i[1]
            if cost2 < distance[i[0]]:
                distance[i[0]] = cost2
                heapq.heappush(queue, (cost2, i[0]))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append([to_, weight])
    graph[to_].append([from_, weight])

dijikstra(1)
print(distance[n])
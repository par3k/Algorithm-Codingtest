# 특정한 최단 경로
import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e9)
n, e = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

v1, v2 = map(int, input().split())


def dijikstra(s):
    queue = list()
    heapq.heappush(queue, (0, s))
    distance = [INF] * (n + 1)
    distance[s] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for cost2, now2 in edges[now]:
            cost3 = cost + cost2
            if distance[now2] > cost3:
                distance[now2] = cost3
                heapq.heappush(queue, (cost3, now2))
    return distance


ans = INF
a = dijikstra(1)[v1]
b = dijikstra(v1)[v2]
c = dijikstra(v2)[n]

d = dijikstra(1)[v2]
e = dijikstra(v2)[v1]
f = dijikstra(v1)[n]
ans = min(ans, a + b + c, d + e + f)

if ans >= INF:
    print(-1)
else:
    print(ans)
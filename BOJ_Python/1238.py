# 파티
# 27721418	hoijae0194	 1238	맞았습니다!!	31612	2452	Python 3 / 수정	842
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)
n, m, x = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))


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


ans = 0
for i in range(1, n + 1):
    go = dijikstra(i)[x]
    back = dijikstra(x)[i]
    ans = max(ans, go + back)
print(ans)

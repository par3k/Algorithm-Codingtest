# 해킹
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


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dijikstra(c)
    cnt, ans = 0, 0

    for i in range(1, len(distance)):
        if distance[i] != INF:
            cnt += 1
            ans = max(ans, distance[i])

    print(cnt, ans)

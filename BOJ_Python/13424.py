# 비밀 모임
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()


def dijikstra(start):
    queue = list()
    heapq.heappush(queue, [0, start])
    distance[start] = 0

    while queue:
        cost, current = heapq.heappop(queue)
        if distance[current] < cost: continue
        for i in graph[current]:
            cost2 = cost + i[1]
            if distance[i[0]] > cost2:
                distance[i[0]] = cost2
                heapq.heappush(queue, [cost2, i[0]])


INF = int(1e9)
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        from_, to_, weight = map(int, input().split())
        graph[from_].append([to_, weight])
        graph[to_].append([from_, weight])

    k = int(input())
    people = list(map(int, input().split()))

    total = [0] * (n + 1)
    for i in people:
        distance = [INF] * (n + 1)
        dijikstra(i)
        for j in range(1, n + 1):
            total[j] += distance[j]

    now, answer = INF, 0
    for i in range(1, n + 1):
        if now > total[i]:
            now = total[i]
            answer = i
    print(answer)
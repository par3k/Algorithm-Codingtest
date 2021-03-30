import sys, heapq
input = lambda :sys.stdin.readline().rstrip()


def PrintResult(res):
    print(distance[end])
    print(len(res))
    print(*res)


def trace(start, end):
    res = [end]
    lastTrace[start] = 0
    while lastTrace[end]:
        res.append(lastTrace[end])
        end = lastTrace[end]
    return PrintResult(res[::-1])

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue) #dist: 지금까지 온 거리, now: 현재 기준 시작 버스.
        if distance[now] < dist:
            continue
        for nextCity, nextDist in graph[now]:
            cost = dist + nextDist
            if cost < distance[nextCity]:
                distance[nextCity] = cost
                lastTrace[nextCity] = now
                heapq.heappush(queue, (cost, nextCity))
    return trace(start, end)


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n + 1)
lastTrace = [None] * (n + 1)
dijkstra(start)
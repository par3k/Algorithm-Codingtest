# 최소비용 구하기
# hoijae0194	 1916	맞았습니다!!	42628	320	Python 3 / 수정	834
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input()) # 노드
m = int(input()) # 엣지
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((to_, weight))

start, end = map(int, input().split())


def dijkstra(start):
    queue = list()
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    while queue:
        now, cost = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for now2, cost2 in graph[now]:
            cost3 = cost + cost2
            if distance[now2] > cost3:
                distance[now2] = cost3
                heapq.heappush(queue, (now2, cost3))

# print(graph)
dijkstra(start)
# print(distance)
print(distance[end])


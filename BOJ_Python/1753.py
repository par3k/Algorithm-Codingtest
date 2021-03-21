from heapq import heappush, heappop

def dijkstra(s):
    pq = []
    d = [123456789] * (v + 1)
    d[s] = 0
    heappush(pq, (d[s], s))
    while pq:
        cur_d, cur_node = heappop(pq)
        if d[cur_node] < cur_d:
            continue
        for dis, next_node in graph[cur_node]:
            if cur_d + dis < d[next_node]:
                d[next_node] = cur_d + dis
                heappush(pq, (d[next_node], next_node))
    return d

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)


for _ in range(e):
    from_, to_, weight_ = map(int, input().split())
    graph[from_].append((to_, weight_))

for i in dijkstra(k)[1:]:
    if i == 123456789:
        print("INF")
    else:
        print(i)
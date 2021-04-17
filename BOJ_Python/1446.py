# 지름길
import sys
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)

n, d = map(int, input().split())
graph = list()

for _ in range(n):
    from_, to_, weight = map(int, input().split())
    if to_ <= d:
        graph.append([from_, to_, weight])

position = [i for i in range(d + 1)]
for i in range(d + 1):
    if i != 0:
        position[i] = min(position[i], position[i - 1] + 1)

    for j in graph:
        if j[0] == i:
            position[j[1]] = min(position[j[1]], position[j[0]] + j[2])
print(position[d])
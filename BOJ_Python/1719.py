# 택배
import sys
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]
stopover = [[0] * n for _ in range(n)]

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_ - 1][to_ - 1] = weight
    graph[to_ - 1][from_ - 1] = weight
    stopover[from_ - 1][to_ - 1] = to_
    stopover[to_ - 1][from_ - 1] = from_

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] == 0
            stopover[i][j] = -1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                stopover[i][j] = stopover[i][k]

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end = ' ')
        else:
            print(stopover[i][j], end=' ')
    print()
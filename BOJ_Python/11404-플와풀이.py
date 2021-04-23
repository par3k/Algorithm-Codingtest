import sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_][to_] = min(graph[from_][to_], weight)


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF: graph[i][j] = 0 # 틀린 이유
        print(graph[i][j], end=' ')
    print()
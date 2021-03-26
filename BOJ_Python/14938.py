# 서강그라운드
# 27632719	hoijae0194	 14938	맞았습니다!!	28776	536	Python 3 / 수정	678
import sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)

n, m, r = map(int,input().split())
items = list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += items[j - 1]

    ans = max(ans, tmp)

print(ans)
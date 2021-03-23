# 특정 거리의 도시 찾기
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
visited[x] = 0
ans = list()

for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        continue
    graph[a].append(b)

queue = deque([x])
while queue:
    cur = queue.popleft()
    for next in graph[cur]:
        if visited[next] == -1:
            visited[next] = visited[cur] + 1
            queue.append(next)

for i in range(n + 1):
    if visited[i] == k:
        ans.append(i)

ans = sorted(ans)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
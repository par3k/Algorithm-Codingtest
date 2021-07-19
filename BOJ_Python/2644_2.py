# 촌수계산
from collections import deque

n = int(input())
a, b = map(int, input().split())

family_tree = [[] for _ in range(n + 1)]
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    family_tree[x].append(y)
    family_tree[y].append(x)

answer = [0 for _ in range(n + 1)]


def bfs(node):
    queue = deque()
    queue.append(node)
    visited = [0 for _ in range(n + 1)]
    visited[node] = 1

    while queue:
        x = queue.popleft()
        for i in family_tree[x]:
            if not visited[i]:
                visited[i] =1
                answer[i] = answer[x] + 1
                queue.append(i)


bfs(a)
if answer[b] != 0:
    print(answer[b])
else:
    print(-1)
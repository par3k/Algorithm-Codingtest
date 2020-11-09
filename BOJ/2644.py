# 촌수계산
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a, b = map(int, input().split())
m = int(input())
s = [[] for _ in range(n + 1)]

family_ship = [0 for _ in range(n + 1)]


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while queue:
        x = queue.popleft()
        for i in s[x]:
            if visited[i] == 0:
                visited[i] = 1
                family_ship[i] = family_ship[x] + 1
                queue.append(i)


for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)
print(s)
bfs(a)

print(family_ship[b] if family_ship[b] != 0 else -1)
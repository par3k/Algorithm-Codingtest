# 정프 점프
from collections import deque

n = int(input())
if n == 1:
    print(0)
    exit()

arr = list(map(int, input().split()))
visited = [0] * n

def bfs(x):
    queue = deque()
    queue.append((x))

    while queue:
        x = queue.popleft()
        jump = arr[x]

        for i in range(1, jump + 1):
            nx = x + i
            if nx < n and not visited[nx]:
                queue.append((nx))
                visited[nx] = visited[x] + 1
                
bfs(0)
print(visited[-1] if visited[-1] else -1)
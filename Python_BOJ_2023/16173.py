# 점프왕 쩰리(Samll)
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [1, 0], [0, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        jump = graph[x][y]
        if graph[x][y] == -1:
            print("HaruHaru")
            exit()
        for i  in range(2):
            nx, ny = x + dx[i] * jump, y + dy[i] * jump
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

bfs()
print("Hing")
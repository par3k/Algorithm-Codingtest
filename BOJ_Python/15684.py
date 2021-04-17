# 드래곤 커브
import sys
input = lambda : sys.stdin.readline().rstrip()
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 우 상 좌 하

n = int(input())
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split()) # x, y 좌표, 방향, 세대
    graph[x][y] = 1
    direction = [d]
    for _ in range(g): # 세대만큼 반복
        tmp = list()
        for i in range(len(direction)):
            tmp.append((direction[- i - 1] + 1) % 4)
        direction.extend(tmp)
        print(direction)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
                ans += 1

print(ans)
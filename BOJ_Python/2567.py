# 색종이 - 2
graph = [[0] * 101 for _ in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
                graph[i][j] = 1

ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if graph[nx][ny] == 0 or nx < 0 or nx > 100 or ny < 0 or ny > 100:
                    ans += 1

print(ans)
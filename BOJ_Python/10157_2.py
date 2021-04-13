import sys
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
C, R = map(int, input().split())
K = int(input())
graph = [[0] * C for _ in range(R)]

x, y = R - 1, 0
cnt, idx = 1, 0

if C * R < K:
    print(0)
    exit(0)

while cnt != K:
    graph[x][y] = cnt
    nx, ny = x + dx[idx], y + dy[idx]

    if 0 > nx or 0 > ny or nx >= R or ny >= C or graph[nx][ny] != 0:
        idx += 1
        if idx > 4: idx = 0
        nx, ny = x + dx[idx], y + dy[idx]

    x, y = nx, ny
    cnt += 1

print(y + 1, R - x)
import sys
input = lambda :sys.stdin.readline().rstrip()

c, r = map(int, input().split())
k = int(input())
graph = [[0] * c for _ in range(r)]

if r * c < k:
    print(0)
    exit()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y, dir = r - 1, 0, 0
cnt = 1

while cnt != k:
    graph[x][y] = cnt
    nx, ny = x + dx[dir], y + dy[dir]

    if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] != 0:
        dir += 1
        if dir == 4: dir = 0
        nx, ny = x + dx[dir], y + dy[dir]

    x, y, cnt = nx, ny , cnt + 1

print(f'{y + 1} {r - x}')
C, R = map(int, input().split())
k = int(input())
arr = [[0] * C for _ in range(R)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = R - 1, 0
cnt, d = 1, 0

if C * R < k:
    print(0)
    exit(0)

while cnt != k:
    arr[x][y] = cnt
    nx, ny = x + dx[d], y + dy[d]
    if arr[nx][ny] != 0 or 0 > nx or 0 > ny or nx >= R or ny >= C:
        d = (d + 1) % 4
        nx, ny = x + dx[d], dy[d]
    x, y = nx, ny
    cnt += 1

print(y + 1, R - x)
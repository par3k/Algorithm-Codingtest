N, M = map(int, input().split())

d = [[0] * M for _ in range(N)]

x, y , di = map(int, input().split())
d[x][y] = 1

array = []

for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global di
    di -= 1
    if di == -1:
        di = 3
    return di

cnt = 1
turn_cnt = 0

while True:
    turn_left()
    nx = x + dx[di]
    ny = y + dy[di]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nx = x - dx[di]
        ny = y - dy[di]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_cnt = 0
print(cnt)
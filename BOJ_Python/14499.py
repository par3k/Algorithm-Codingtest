# 주사위 굴리기
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M, x, y, K = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))


class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.east = 0
        self.west = 0
        self.north = 0
        self.south = 0


dice = Dice()

for i in cmd:
    if i == 1:
        dx, dy = 0, 1
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            dice.east, dice.bottom, dice.west, dice.top = dice.top, dice.east, dice.bottom, dice.west

            if graph[nx][ny] == 0:
                graph[nx][ny] = dice.bottom
            else:
                dice.bottom = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice.top)
            x, y = nx, ny

    elif i == 2:
        dx, dy = 0, -1
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            dice.west, dice.bottom, dice.east, dice.top = dice.top, dice.west, dice.bottom, dice.east

            if graph[nx][ny] == 0:
                graph[nx][ny] = dice.bottom
            else:
                dice.bottom = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice.top)
            x, y = nx, ny

    elif i == 3:
        dx, dy = -1, 0
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            dice.north, dice.bottom, dice.south, dice.top = dice.top, dice.north, dice.bottom, dice.south

            if graph[nx][ny] == 0:
                graph[nx][ny] = dice.bottom
            else:
                dice.bottom = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice.top)
            x, y = nx, ny

    elif i == 4:
        dx, dy = 1, 0
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            dice.south, dice.top, dice.north, dice.bottom = dice.top, dice.north, dice.bottom, dice.south
            if graph[nx][ny] == 0:
                graph[nx][ny] = dice.bottom
            else:
                dice.bottom = graph[nx][ny]
                graph[nx][ny] = 0
            print(dice.top)
            x, y = nx, ny
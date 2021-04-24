# 낚시왕
import sys
input = lambda :sys.stdin.readline().rstrip()
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] # 상,하,우,좌


def sharkMove():
    tmp = [[0] * C for _ in range(R)] # tmp에 새로 저장을 해줘서 return 해줄것이다.

    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0: # 상어가 있으면
                x, y, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]

                while s > 0: # 속도만큼 이동해야 하므로 while 을 써서 한칸씩 dx, dy 이동
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1 # 기저 조건 만들어 주려고 s -= 1해줌
                    else: # 지도 밖으로 나가면 방향 전환을 해줘야 됨
                        x -= dx[d] # 빠꾸
                        y -= dy[d]

                        if d == 0: d = 1 # 방향도 뒤집어 줘야됨 상 > 하
                        elif d == 1: d = 0 # 하 > 상
                        elif d == 2: d = 3 # 우 > 좌
                        elif d == 3: d = 2 # 좌 > 우

                if tmp[x][y] == 0: # 새로 이동한 맵에다
                    tmp[x][y] = [graph[i][j][0], d, z] # 상어 정보 정리
                else: # 상어가 있으면
                    if tmp[x][y][2] < z: # 사이즈 비교후 큰것을
                        tmp[x][y] = [graph[i][j][0], d, z] # 위치 시킴
    return tmp # 이렇게 새로 짠 그래프를 보냄


R, C, m = map(int, input().split()) # 격자판 크기, 상어의 수
graph = [[0] * C for _ in range(R)]

for _ in range(m):
    r, c, s, d, z = map(int, input().split())
    graph[r - 1][c - 1] = [s, d - 1, z] #속력, 방향, 크기 저장

ans = 0
for i in range(C):
    for j in range(R):
        if graph[j][i] != 0: # 가장 가까이에 있는 상어를 일단 잡음
            ans += graph[j][i][2]
            graph[j][i] = 0 # 잡고 지도에서 지워주기
            break
    graph = sharkMove()

print(ans)
# 파이프 옮기기 1
import sys
input = lambda : sys.stdin.readline().rstrip()


def dfs(pos):
    global cnt
    x, y, z = pos # x, y좌표 , 방향

    # 0 : ㅡ
    # 1 : ㅣ
    # 2 : \

    if x == n - 1 and y == n - 1: # 기저 조건
        cnt += 1
        return

    if x + 1 < n and y + 1 < n:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0: # 이동할 수 있으면
            dfs((x + 1, y + 1, 2))

    if z == 0 or z == 2:
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, 0))

    if z == 1 or z == 2:
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, 1))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs((0, 1, 0)) # 방향은 ㅡ 로 시작
print(cnt)

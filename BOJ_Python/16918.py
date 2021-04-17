# 봄버맨
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def findBomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O': # 폭탄의 위치를 확인
                bombList.append((i, j))


# 3단계 : 모든 칸에 폭탄을 설치한다.
def allBombSet():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'


# 4단계 : 폭탄이 터진다.
def bomb():
    while bombList:
        x, y = bombList.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = '.'


r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)] # 1단계 : 폭탄을 설치
n -= 1 # 2단계 : 아무것도 하지않고 시간만 감
while n:
    bombList = deque()
    findBomb()
    allBombSet()
    n -= 1
    if n == 0:
        break
    bomb()
    n -= 1

for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()
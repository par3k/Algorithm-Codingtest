# 미세먼지 안녕!
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
purifier = -1

for i in range(r):
    for j in range(c):
        if purifier == -1 and graph[i][j] == -1:
            purifier = i
queue = deque()


def findDust():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1 or graph[i][j] == 0: continue
            queue.append([i, j, graph[i][j]])


def spreadDust():
    while queue:
        x, y, dustSum = queue.popleft()
        if dustSum < 5: continue
        amountOfDust = dustSum // 5
        howManySpreadCnt = 0

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == -1: continue
                graph[nx][ny] += amountOfDust
                howManySpreadCnt += 1
        graph[x][y] -= amountOfDust * howManySpreadCnt


def runningPurifier():
    top, bottom = purifier, purifier + 1

    for i in range(top - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]
    for i in range(c - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(top):
        graph[i][c - 1] = graph[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[top][i] = graph[top][i - 1]
    graph[top][1] = 0

    for i in range(bottom + 1, r - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(c - 1):
        graph[r - 1][i] = graph[r - 1][i + 1]
    for i in range(r - 1, bottom, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        graph[bottom][i] = graph[bottom][i - 1]
    graph[bottom][1] = 0


for tc in range(t):
    findDust()
    spreadDust()
    runningPurifier()

answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            answer += graph[i][j]

print(answer)
# 톱니바퀴
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


def cw_rotate(n, dir, graph):
    if n == 4: return

    if graph[n - 1][2] != graph[n][6]:
        cw_rotate(n + 1, -dir, graph)
        graph[n].rotate(dir)
    else:
        return


def ccw_rotate(n, dir, graph):
    if n == -1: return

    if graph[n + 1][6] != graph[n][2]:
        ccw_rotate(n - 1, -dir, graph)
        graph[n].rotate(dir)
    else:
        return


graph = [deque(map(int, input())) for _ in range(4)]
for _ in range(int(input())):
    num, wise = map(int, input().split())
    cw_rotate(num, -wise, graph)
    ccw_rotate(num - 2, -wise, graph)
    graph[num - 1].rotate(wise)

ans = 0
for i in range(4):
    ans += (2 ** i) * graph[i][0]
print(ans)
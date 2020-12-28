# 맥주 마시면서 걸어가기
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


def check(point1, point2):
    dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    if dist <= 1000:
        return True
    else:
        return False


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        pos = queue.popleft()
        for i in edges[pos]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


for _ in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n + 2)]
    edges = [[] for _ in range(n + 2)]
    visited = [False for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i != j:
                if check(graph[i], graph[j]):
                    edges[i].append(j)
    bfs(0)

    if visited[n + 1]:
        print("happy")
    else:
        print("sad")
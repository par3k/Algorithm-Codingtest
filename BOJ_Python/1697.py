# 숨바꼭질
from collections import deque
import sys

n , k = map(int, sys.stdin.readline().rstrip().split())
visited = [0] * 100001


def bfs(n, k, visited):
    queue = deque()
    queue.append(n)

    while queue:
        nowPosition = queue.popleft()
        if nowPosition == k:
            print(visited[nowPosition])
            break

        arr = [nowPosition - 1, nowPosition + 1, nowPosition * 2]

        for newPosition in arr:
            if 0 <= newPosition <= 100000 and visited[newPosition] == 0:
                visited[newPosition] = visited[nowPosition] + 1
                queue.append(newPosition)


bfs(n, k, visited)
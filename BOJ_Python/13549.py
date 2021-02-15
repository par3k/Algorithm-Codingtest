# 숨바꼭질 3
import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            return arr[x]

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < 100001 and not arr[nx]:
                if nx == 2 * x and x != 0:
                    arr[nx] = arr[x] + 1
                    queue.appendleft(nx)
                else:
                    arr[nx] = arr[x] + 1
                    queue.append(nx)


n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [0] * 100001
print(bfs(n))
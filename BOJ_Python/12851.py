# 숨바꼭질 2
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [[100001, 0] for _ in range(100001)]
arr[n][0], arr[n][1] = 0, 1


queue = deque([n])
while queue:
    x = queue.popleft()

    for nx in [x - 1, x + 1, 2 * x]:
        if 0 <= nx < 100001:
            if arr[nx][0] == 100001:
                queue.append(nx)
                arr[nx][0] = arr[x][0] + 1
                arr[nx][1] = arr[x][1]
            elif arr[nx][0] == arr[x][0] + 1:
                arr[nx][1] += arr[x][1]


print(arr[k][0])
print(arr[k][1])
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = [0] * 100001
prev_node = [0] * 100001


def save_path(x):
    path_arr = list()
    tmp = x
    for _ in range(arr[x] + 1):
        path_arr.append(tmp)
        tmp = prev_node[tmp]
    print(' '.join(map(str, path_arr[::-1])))


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(arr[x])
            save_path(x)
            return x

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < len(arr) and not arr[nx]:
                queue.append(nx)
                arr[nx] = arr[x] + 1
                prev_node[nx] = x


bfs()
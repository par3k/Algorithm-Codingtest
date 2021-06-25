# 회전하는 큐
import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = deque(i+1 for i in range(N))
target = deque(map(int, input().split()))

cnt = 0
while target:
    t = target.popleft()
    idx = 0
    for i in range(len(arr)):
        if arr[i] == t:
            idx = i

    if 0 < idx <= len(arr) // 2: # arr배열의 왼쪽에 있다면
        while idx:
            arr.append(arr.popleft())
            cnt += 1
            idx -= 1
            if idx == -1:
                idx = len(arr) - 1
        if arr[0] == t:
            arr.popleft()
    elif len(arr) // 2 < idx < len(arr): # arr배열의 오른쪽에 있다면
        while idx:
            arr.appendleft(arr.pop())
            cnt += 1
            idx += 1
            if idx == len(arr):
                idx = 0
        if arr[0] == t:
            arr.popleft()
    else:
        arr.popleft()
print(cnt)
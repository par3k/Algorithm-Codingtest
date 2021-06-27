# 카드 놓기
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
cmd = deque(map(int, input().split()))
res = deque(range(1, n + 1))
ans = deque()

while cmd:
    a = cmd.pop()
    b = res.popleft()

    if a == 1:
        ans.appendleft(b)
    elif a == 2:
        ans.insert(1, b)
    elif a == 3:
        ans.append(b)

print(' '.join(map(str, ans)))
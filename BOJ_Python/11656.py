# 접미사 배열
import sys
from collections import deque

s = deque(sys.stdin.readline().rstrip())
ans = [''.join(s)]

for i in range(len(s)):
    s.popleft()
    ans.append(''.join(s))

ans.pop()
ans.sort()

for i in ans:
    print(i)
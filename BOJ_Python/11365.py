# !밀비 급일
import sys
from collections import deque

while True:
    s = sys.stdin.readline().rstrip()
    if s == 'END': break

    tmp = deque()
    for i in range(len(s)):
        tmp.appendleft(s[i])

    print(''.join(tmp))
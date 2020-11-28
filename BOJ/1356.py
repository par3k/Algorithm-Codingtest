# 유진수
import sys

s = sys.stdin.readline().rstrip()
ans = 0
for i in range(len(s)):
    if s == '1': continue
    forward = s[0:i + 1]
    backward = s[i + 1:len(s) + 1]

    x = 1
    for j in forward:
        x *= int(j)

    y = 1
    for j in backward:
        y *= int(j)

    if x == y:
        ans += 1

if ans >= 1:
    print('YES')
else:
    print('NO')
# 그릇
import sys
s = list(map(str, sys.stdin.readline().rstrip()))

ans = 10
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        ans += 5
    else:
        ans += 10
print(ans)
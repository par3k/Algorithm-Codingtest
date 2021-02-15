# 모음의 개수
import sys

s = sys.stdin.readline().rstrip()
a = ['a', 'e', 'i', 'o', 'u']

ans = 0

for i in range(len(s)):
    for j in a:
        if s[i] == j:
            ans += 1

print(ans)
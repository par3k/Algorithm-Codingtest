# 반지
import sys
input = lambda : sys.stdin.readline().rstrip()

ans = 0
find = input()

for i in range(int(input())):
    s = input()
    if find in s:
        ans += 1
    else:
        for i in range(1, len(find)):
            if s[-(len(find) - i):] + s[:i] == find:
                ans += 1

print(ans)
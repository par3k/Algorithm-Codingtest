# JOI와 IOI
import sys
input = lambda: sys.stdin.readline().rstrip()

s = list(map(str, input()))
ans = [0] * 2

for i in range(len(s) - 2):
    if s[i] == 'J':
        if s[i + 1] == 'O' and s[i + 2] == 'I':
            ans[0] += 1

    elif s[i] == 'I':
        if s[i + 1] == 'O' and s[i + 2] == 'I':
            ans[1] += 1

print(ans[0])   # 'JOI'
print(ans[1])   # 'IOI'
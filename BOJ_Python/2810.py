# 컵홀더
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(input().upper())

ans = ['*']

for c in arr:
    if c == 'S':
        ans.append(c)
        ans.append('*')

    elif c == 'L':
        if ans[-1] == 'L':
            ans.append(c)
            ans.append('*')
        else:
            ans.append(c)

n_couple = ans.count('*')

if n < n_couple:
    print(n)
else:
    print(n_couple)
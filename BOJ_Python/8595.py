# 히든 넘버
import sys
input = lambda : sys.stdin.readline().rstrip()

number = '0123456789'
n = int(input())
s = input()
tmp = ''
ans = 0

for i in range(n):
    if s[i] in number:
        tmp += s[i]
    else:
        tmp += ' '

arr = list(map(str, tmp.split(' ')))
for j in range(len(arr)):
    if arr[j] != '':
        ans += int(arr[j])
print(ans)

# 소수 단어
import sys

tmp, ans = sys.stdin.readline().rstrip(), 0

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(tmp)):
    if tmp[i] in lower:
        ans += (ord(tmp[i]) - 96)
    elif tmp[i] in upper:
        ans += (ord(tmp[i]) - 64 + 26)

p = 0
for i in range(2, ans):
    if ans % i == 0:
        p += 1

if p == 0:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
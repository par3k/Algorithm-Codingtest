# Hashing
import sys
input = lambda : sys.stdin.readline().rstrip()

l, tmp, ans = int(input()), input(), 0

for i in range(l):
    ans += (ord(tmp[i]) - 96) * (31 ** i)

print(ans % 1234567891)
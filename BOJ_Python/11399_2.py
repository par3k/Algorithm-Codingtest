# ATM
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
p = list(map(int, input().split()))
p.sort()

ans = 0

for i in range(n):
    ans += sum(p[:i + 1])

print(ans)
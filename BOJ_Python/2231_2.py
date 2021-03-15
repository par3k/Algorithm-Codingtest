# 분해합
import sys
n = int(sys.stdin.readline().rstrip())


def function(n):
    ans = n
    while n > 0:
        tmp = n % 10
        n = n // 10
        ans += tmp
    return ans


k = 0
for i in range(int(n * 0.80), n + 1):
    if function(i) == n:
        k = i
        break
print(k)
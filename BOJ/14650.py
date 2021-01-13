# 걷다보니 신천역 삼
import sys
sys.setrecursionlimit(10000000)

N = int(sys.stdin.readline().rstrip())
ans = 0


def calc(n, sum):
    global ans
    for i in range(3):
        if n == 0 and i == 0:
            continue
        if n == N:
            if sum % 3 == 0:
                ans += 1
                return ans
        else:
            calc(n + 1, sum + i)


calc(0, 0)
print(ans)
# 우울한 방학
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def cal_sad(n):
    sad = 1
    result = 0
    while sad <= n:
        result += sad * sad
        sad += 1
    return result


sad_sum = m - n - sum(arr)
sum = sad_sum // (n + 1)
rest = sad_sum % (n + 1)

print(cal_sad(sum) * (n + 1 - rest) + cal_sad(sum + 1) * rest)
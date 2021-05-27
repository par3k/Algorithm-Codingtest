# 피보나치 함수
import sys
input = lambda : sys.stdin.readline().rstrip()

def fibonacci_cnt(n):
    zero_cnt = [1, 0]
    one_cnt = [0, 1]
    if n <= 1:
        return

    for i in range(2, n + 1):
        zero_cnt.append(zero_cnt[i - 1] + zero_cnt[i - 2])
        one_cnt.append(one_cnt[i - 1] + one_cnt[i - 2])

    return zero_cnt, one_cnt

zero_count, one_count = fibonacci_cnt(40)

for _ in range(int(input())):
    m = int(input())
    print(f'{zero_count[m]} {one_count[m]}')
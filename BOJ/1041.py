# 주사위
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a, b, c, d, e, f = map(int, input().split())

if n == 1:
    print(sum([a, b, c, d, e, f]) - max([a, b, c, d, e, f]))

else:
    three_cnt = min(list(map(sum, [[a, b, c], [a, b, d], [a, e, d], [a, e, c], [f, b, c], [f, b, d], [f, e, c], [f, e, d]])))
    two_cnt = min(list(map(sum, [[a, b], [a, c], [a, d], [a, e], [b, c], [b, d], [e, c], [e, d], [f, b], [f, c], [f, e], [f, d]])))
    one_cnt = min([a, b, c, d, e, f])

    print(three_cnt * 4 + two_cnt * (8 * n - 12) + one_cnt * ((n - 2) * (5 * n - 6)))
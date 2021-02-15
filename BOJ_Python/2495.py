# 연속 구간
import sys
input = lambda : sys.stdin.readline().rstrip()


def cnt(s):
    cnt = 1
    max_cnt = 1
    compare = s[0]

    for n in s[1:]:
        if n == compare:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            compare = n
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt


for _ in range(3):
    print(cnt(input()))
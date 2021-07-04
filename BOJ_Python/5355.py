# 화성 수학
import sys
input = lambda :sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(input().split())

    for i in range(len(s)):
        if s[i] == '@':
            s[0] = float(s[0]) * 3
        elif s[i] == '%':
            s[0] = float(s[0]) + 5
        elif s[i] == '#':
            s[0] = float(s[0]) - 7
    ans = s[0]
    print(format(round(ans, 3), ".2f"))
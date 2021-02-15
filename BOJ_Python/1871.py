# 좋은 자동차 번호판
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(input().split('-'))
    ans = 0

    for i in range(3):
        ans += (ord(s[0][i]) - 65) * 26 ** (2 - i)

    if abs(ans - int(s[1])) <= 100:
        print('nice')
    else:
        print('not nice')
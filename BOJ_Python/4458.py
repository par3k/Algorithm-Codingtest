# 첫 글자를 대문자로
import sys
input = lambda :sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(map(str, input()))
    s[0] = s[0].upper()
    print(''.join(s))
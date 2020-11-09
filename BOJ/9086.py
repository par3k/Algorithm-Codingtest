# 문자열
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    print(s[0]+s[-1])
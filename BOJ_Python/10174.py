# 팰린드롬
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(map(str, input().lower()))
    print('Yes' if s[::] == s[::-1] else 'No')
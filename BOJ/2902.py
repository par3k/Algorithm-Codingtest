# KMP는 왜 KMP일까?
import sys
s = sys.stdin.readline().rstrip().split('-')

for i in range(len(s)): print(s[i][0], end='')
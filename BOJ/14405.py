# 피카츄
import sys

s = sys.stdin.readline().rstrip()
s = s.replace('pi', ' ').replace('ka', ' ').replace('chu', ' ')
print('YES' if s.strip() == '' else 'NO')
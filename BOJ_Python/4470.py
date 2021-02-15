# 줄번호
import sys
input = lambda : sys.stdin.readline().rstrip()

for i in range(int(input())):
    s = input()
    print(f'{i + 1}. {s}')

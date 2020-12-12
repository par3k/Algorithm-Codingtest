# 스캐너
import sys
input = lambda : sys.stdin.readline().rstrip()

r, c, zr, zc = map(int, input().split())
arr = [input() for _ in range(r)]

for s in arr:
    s = ''.join(char * zc for char in s)
    for _ in range(zr):
        print(s)
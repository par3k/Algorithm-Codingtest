# 디지털 티비

import sys

n = int(sys.stdin.readline().rstrip())

channels = [sys.stdin.readline().rstrip() for _ in range(n)]


for i in range(n):
    if channels[i] == 'KBS1':
        idx1 = i
    elif channels[i] == 'KBS2':
        idx2 = i


if idx1 > idx2:
    idx2 += 1

print('1' * idx1 + '4' * idx1 + '1' * idx2 + '4' * (idx2-1))
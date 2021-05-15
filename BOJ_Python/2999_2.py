import sys
n = list(map(str, sys.stdin.readline().rstrip()))

text_len = len(n)

R, C = 0, 0
tmp = list()

for i in range(1, text_len + 1):
    if text_len % i == 0 and i <= text_len // i:
        R = max(R, i)
        C = text_len // R

arr = [['.'] * C for _ in range(R)]
idx = 0

for i in range(C):
    for j in range(R):
        arr[j][i] = n[idx]
        idx += 1

for i in range(R):
    for j in range(C):
        print(''.join(arr[i][j]), end='')
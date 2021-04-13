# 비밀 이메일

a = list(map(str,input()))
a_len = len(a)
R, C = 0, 0

for i in range(1, a_len + 1):
    if a_len % i == 0 and i <= a_len // i:
        R = max(R, i)
        C = a_len // R

arr = [['.'] * C for _ in range(R)]

idx = 0

for j in range(C):
    for i in range(R):
        arr[i][j] = a[idx]
        idx += 1

for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')

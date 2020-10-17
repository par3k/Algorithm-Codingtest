# 베르트랑 공준
import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0: break

    arr = [0] * (2 * n + 1)
    ans = 0

    for i in range(2, 2 * n + 1):
        if arr[i] == 0:
            if i > n: ans += 1
            for j in range(i, 2 * n + 1, i):
                arr[j] = 1
    print(ans)
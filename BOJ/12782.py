# 비트 우정지수
import sys
input = lambda :sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr = list(map(str, input().split()))
    n, m = arr[0], arr[1]
    one, zero = 0, 0
    for i in range(len(m)):
        if n[i] == m[i]: continue
        if m[i] == '1':
            one += 1
        else:
            zero += 1

    t = min(one, zero)
    print(t + (one + zero) - t * 2)

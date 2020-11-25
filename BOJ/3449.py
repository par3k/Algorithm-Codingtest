# 해밍 거리
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a, b = input(), input()
    ans = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1

    print(f'Hamming distance is {ans}.')
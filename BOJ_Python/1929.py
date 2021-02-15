# 소수 구하기
import sys
input = lambda : sys.stdin.readline().rstrip()

m, n = map(int, input().split())

arr = [0] * (n + 1)

for i in range(2, n+1):
    if arr[i] == 0:
        if i >= m: print(i)
        for j in range(i, n+1, i): # i의 배수로 순환함
            arr[j] = 1

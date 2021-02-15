# 수 정렬하기 3 - 계수정렬
import sys

n = int(sys.stdin.readline())
counts = [0] * 10001

for i in range(n):
    tmp = int(sys.stdin.readline())
    counts[tmp] += 1

for i in range(len(counts)):
    for j in range(counts[i]):
        print(i)
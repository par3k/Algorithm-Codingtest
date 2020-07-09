import sys

sys.stdin = open("/Users/alex/Documents/GitHub/codingtest/input.txt", "rt")
n, m = list(map(int, input().split()))

cnt = [0] * (n+m+3)
max = -21470000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')

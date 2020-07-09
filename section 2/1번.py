# K번째 약수

import sys
sys.stdin = open("../input.txt", "rt")
n, k = map(int, input().split())
count = 0

for i in range(1, n+1): # range(1, n+1) 이거를 잊지 말기
    if n % i == 0:
        count += 1

    if count == k:
        print(i)
        break
else:
    print(-1)

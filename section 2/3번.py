# K번째 큰수

import sys
sys.stdin = open("../input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = set()

for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            result.add(a[i]+a[j]+a[z])
result = list(result)
# print(result)
result.sort(reverse=1)
# print(result)
print(result[k-1])


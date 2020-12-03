# 부분수열의 합
from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, n + 1):
    for cb in combinations(arr, i):
        if sum(cb) == s:
            ans += 1
print(ans)
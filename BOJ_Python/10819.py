from itertools import permutations
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
input = list(map(int, input().split()))

ans = 0
for i in permutations(input):
    tmp = list(i)
    max_ = 0
    for i in range(0, len(tmp) - 1):
        max_ += abs(tmp[i] - tmp[i + 1])
    if max_ > ans:
        ans = max_

print(ans)
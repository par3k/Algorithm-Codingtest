# 가장 긴 증가하는 부분 수열4
# 27688564	hoijae0194	 14002	맞았습니다!!	32704	172	Python 3 / 수정	447
from collections import deque

n = int(input())
A = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))

idx = dp.index(max(dp))
c = dp[idx]
queue = deque()

for i in range(idx-1, -1, -1):
    if c == dp[i] + 1:
        c = dp[i]
        queue.appendleft(A[i])
queue.append(A[idx])


print(' '.join(map(str, queue)))
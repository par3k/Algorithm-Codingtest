# 좋은 친구
import sys
input = lambda :sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = list(input() for _ in range(n))

dp = [0] * 21
answer = 0

for i in range(n):
    l = len(arr[i])
    arr[i] = l
    if i > k:
        dp[arr[i - k - 1]] -= 1
    answer += dp[l]
    dp[l] += 1

print(answer)

# answer = 0
# while arr:
#     a = arr.popleft()
#     length = len(a)
#     if len(arr) >= k:
#         for i in range(k):
#             if length == len(arr[i]):
#                 answer += 1
#     else:
#         if len(arr) == 0: break
#         if len(arr.popleft()) == length:
#             answer += 1
# print(answer)
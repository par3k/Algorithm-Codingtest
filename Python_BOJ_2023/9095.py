# 1,2,3 더하기

def find(n):
    dp = [0] * 100
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

nums = list()

for _ in range(int(input())):
    nums.append(int(input()))

for num in nums:
    print(find(num))
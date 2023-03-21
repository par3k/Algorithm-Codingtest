# 파스칼의 삼각형

n, k = map(int, input().split())

dp = list()
dp.append([1])
dp.append([1, 1])

for i in range(3, n + 1):
    tmp = [0] * i # [0, 0, 0] | i = 3
    for j in range(i): # j = 0, 1 ,2 | i = 3
        if j == 0:
            tmp[j] = 1
        elif j == i - 1:
            tmp[j] = 1
        else:
            tmp[j] = dp[i - 2][j - 1] + dp[i - 2][j]
    dp.append(tmp)
print(dp[n - 1][k - 1])
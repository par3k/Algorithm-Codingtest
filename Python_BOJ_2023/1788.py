# 피보나치 수의 확장
N = int(input())

if N == 0:
    print(0)
    print(0)
else:
    dp=[0] * (abs(N) + 1)
    dp[1] = 1

    if N < 0:
        for i in range(2, abs(N) + 1):
            dp[i]=(dp[i - 2] - dp[i - 1])
            if dp[i] < 0:
                dp[i] %= -1000000000
            else:
                dp[i] %= 1000000000
    elif N > 0:
        for i in range(2, N + 1):
            dp[i] = (dp[i - 1] % 1000000000 + dp[i - 2] % 1000000000)

    if N < 0:
        if dp[-N] < 0:
            print(-1)
            print(abs(dp[-N] % -1000000000))
        else:
            print(1)
            print(dp[-N] % 1000000000)
    elif N > 0:
        print(1)
        print(dp[N] % 1000000000)
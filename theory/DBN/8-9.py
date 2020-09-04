# 금광

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    idx = 0

    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx += m

    for b in range(1, m):
        for a in range(n):
            # 왼쪽 위에서 오는경우
            if a == 0:
                left_up = 0
            else:
                left_up = dp[a-1][b-1]
            # 왼쪽 아래에서 오는경우
            if a == n-1:
                left_down = 0
            else:
                left_down = dp[a+1][b-1]
            # 왼쪽에서 오는경우
            left = dp[a][b-1]

            dp[a][b] = dp[a][b] + max(left_up, left_down, left)

    ans = 0

    for i in range(n):
        ans = max(ans, dp[i][m-1])

    print(ans)

# 가장 큰 증가 부분 수열
# 27687512	hoijae0194	 11055	맞았습니다!!	28776	180	Python 3 / 수정	217
N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    tmp = 0
    for j in range(i):
        if A[i] > A[j]:
            tmp = max(tmp, dp[j])
    dp[i] = tmp + A[i]

print(max(dp))
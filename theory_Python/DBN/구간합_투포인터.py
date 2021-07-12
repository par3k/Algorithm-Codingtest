m = 5 # 구할 합
arr = [1, 2, 3, 2, 5] # arr값

ans, interval_sum, end = 0, 0, 0
for start in range(len(arr)):
    while interval_sum < m and end < len(arr):
        interval_sum += arr[end]
        end += 1
    if interval_sum == m: ans += 1
    interval_sum -= arr[start]

print(ans)
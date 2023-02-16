# 블랙잭

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
max_val = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = arr[i] + arr[j] + arr[k]
            if max_val <= sum and sum <= m:
                max_val = max(max_val, sum)
print(max_val)
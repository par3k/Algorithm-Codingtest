# 수들의 합2

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start, end = 0, 0

while start <= end <= n:
    tmp = sum(arr[start:end])
    if tmp == m:
        answer += 1
    if tmp <= m:
        end += 1
        continue
    elif tmp > m and start < end:
        start += 1
        continue
    else:
        start += 1
        end += 1

print(answer)
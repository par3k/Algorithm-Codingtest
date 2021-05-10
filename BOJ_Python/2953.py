# 나는 요리사다
import sys

arr, ans, ans_idx = [0] * 5, 0, 0

for i in range(5):
    score = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = sum(score)

for i in range(5):
    if ans < arr[i]:
        ans = arr[i]
        ans_idx = i + 1

print(ans_idx, end=' ')
print(ans)
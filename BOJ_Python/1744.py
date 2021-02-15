# 수 묶기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]

positive = []
negative = []
ans = 0

for i in arr:
    if i <= 0:
        negative.append(i)
    elif i == 1:
        ans += 1
    elif i > 1:
        positive.append(i)

negative.sort()
positive.sort(reverse=True)


for i in range(0, len(positive), 2):
    if i + 1 < len(positive):
        ans += positive[i] * positive[i+1]
    else:
        ans += positive[i]

for i in range(0, len(negative), 2):
    if i + 1 < len(negative):
        ans += negative[i] * negative[i+1]
    else:
        ans += negative[i]

print(ans)
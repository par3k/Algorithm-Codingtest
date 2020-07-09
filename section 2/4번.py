# 대표값

import sys
sys.stdin = open("../input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
print(a)
avg = round(sum(a)/n)
min = 214700000

for idx, x in enumerate(a):
    temp = abs(x - avg)
    print(temp)
    if temp < min:
        min = temp
        score = x
        result = idx + 1
    elif temp == min:
        if x > score:
            score = x
            result = idx + 1
print(avg, result)
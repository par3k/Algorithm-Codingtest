# 소수(에라토스테네스 체)
import sys

sys.stdin = open("/Users/alex/Documents/GitHub/codingtest/input.txt", "rt")
x = int(input())

count = 0

while x > 0:
    if x == 1:
        count = count-1

    for i in range(2, x//2+1):
        if x % i == 0:
            break
    else:
        count = count+1

    x = x-1

print(count)
# 최고의 피자
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
cost = list(map(int, input().split()))
dow_cal = int(input())
topping_cal = [int(input()) for _ in range(n)]

topping_cal.sort(reverse=True)

answer = dow_cal / cost[0]

for i in topping_cal:
    cost[0] += cost[1]
    if (dow_cal + i) / cost[0] > answer:
        dow_cal += i
        answer = dow_cal / cost[0]
    else: break

print(int(answer))
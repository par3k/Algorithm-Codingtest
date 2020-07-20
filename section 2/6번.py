# 자릿수의 합
import sys

sys.stdin = open("/Users/alex/Documents/GitHub/codingtest/input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))


# def digit_sum(x): # 아이디어 정석대로 풀기
#     sum = 0
#     while x>0:
#         sum += x%10
#         x = x//10
#     return sum
#
# max = -2147000000
#
# for x in a:
#     total = digit_sum(x)
#
#     if total > max:
#         max = total
#         result = x
# print(result)


def digit_sum(x):
    sum =0
    for i in str(x):
        sum += int(i)

        return sum

max = -21470000

for x in a:
    total = digit_sum(x)

    if total > max:
        max = total

        result = x

print(result)

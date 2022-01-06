# 팩토리얼
import sys
sys.setrecursionlimit(100000)
insert = int(input())

def factorial(i):
    if i <= 1:
        return 1
    else:
        return i * factorial(i - 1)

print(factorial(insert))
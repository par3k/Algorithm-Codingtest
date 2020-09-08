# 포도주 시식
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

wines = [0]

for _ in range(n):
    wines.append(int(input()))

dp = [0 for _ in range(100001)]


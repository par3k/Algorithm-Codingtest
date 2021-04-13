import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * n for _ in range(n)]


def func(start, end):
    if start >= end: return 1
    if dp[start][end] != -1: return dp[start][end]
    if arr[start] != arr[end]: return 0
    dp[start][end] = func(start + 1, end - 1)
    return dp[start][end]


for i in range(int(input())):
    x, y = map(int, input().split())
    print(func(x - 1, y - 1))
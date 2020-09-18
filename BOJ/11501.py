# 주식
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max = arr[n-1]

    for i in range(n-2, -1, -1):
        if arr[i] < max:
            ans += max - arr[i]
        else:
            max = arr[i]

    t -= 1
    print(ans)
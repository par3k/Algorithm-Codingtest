# 정수 N개의 합

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

a = list(map(int,input().split()))

print(solve(a))
# 연산자 끼워넣기
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
_min, _max = 123456789, -123456789


def dfs(i, res, add, sub, mul, div):
    global _min, _max
    if i == n:
        _max = max(res, _max)
        _min = min(res, _min)
        return

    else:
        if add:
            dfs(i+1, res+arr[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-arr[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*arr[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/arr[i]), add, sub, mul, div-1)


dfs(1, arr[0], add, sub, mul, div)

print(_max)
print(_min)
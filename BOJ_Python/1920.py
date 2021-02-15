# 수 찾기

import sys
input = lambda : sys.stdin.readline().rstrip()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
target = list(map(int, input().split()))

for i in target:
    ans = binary_search(arr, i, 0, n-1)

    if ans != None:
        print(1)
    else:
        print(0)
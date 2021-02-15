# 부품 찾기

N = int(input())
parts = list(map(int, input().split()))
parts.sort()

M = int(input())
order = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return None

for i in order:
    ans = binary_search(parts, i, 0, N-1)
    if ans == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
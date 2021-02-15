# 재귀를 이용한 바이너리 서치


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)

    else:
        return binary_search(arr, target, mid+1, end)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

ans = binary_search(arr, target, 0, n-1)


if ans == None:
    print('None')
else:
    print(ans+1)
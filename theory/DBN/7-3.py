# 반복을 이용한 바이너리 서치


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = end-1

        else:
            start = mid+1

    return None


n, target = map(int, input().split())
arr = list(map(int, input().split()))

ans = binary_search(arr, target, 0, n-1)

if ans == None:
    print('None')

else:
    print(ans+1)
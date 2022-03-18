# 수 찾기
n = int(input())
lis = list(map(int, input().split()))
lis.sort()
m = int(input())
fin = list(map(int, input().split()))

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

for i in fin:
    res = binary_search(lis, i, 0, n - 1)
    if res != None:
        print(1)
    else:
        print(0)
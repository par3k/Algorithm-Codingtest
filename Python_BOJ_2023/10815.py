# 숫자 카드

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))

def bin_search(target):
    global n, m, arr1
    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            return True

        if arr1[mid] < target:
            start = mid + 1
        elif arr1[mid] > target:
            end = mid - 1
    return False

for i in range(m):
    if bin_search(arr2[i]):
        print(1)
    else:
        print(0)
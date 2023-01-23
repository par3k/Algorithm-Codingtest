# 수 찾기

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(num):
    global arr1
    start = 0
    end = len(arr1) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == num:
            return True

        if arr1[mid] < num:
            start = mid + 1
        elif arr1[mid] > num:
            end = mid - 1
        
    return False
        

for i in arr2:
    if binary_search(i):
        print(1)
    else:
        print(0)

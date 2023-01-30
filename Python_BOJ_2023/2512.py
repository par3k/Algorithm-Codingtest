# 예산
n = int(input())
arra = list(map(int, input().split()))
m = int(input())
arra.sort()

def binary_search(arr):
    start = 0
    end = max(arr)
    
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        cnt = 0
        for i in range(n):
            if arr[i] >= mid:
                cnt += mid
            else:
                cnt += arr[i]
        if cnt <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

answer = binary_search(arra)
print(answer)
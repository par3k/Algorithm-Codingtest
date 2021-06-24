# 가장 긴 증가하는 부분 수열5

from bisect import bisect_left

N = int(input())
arr = [0] + list(map(int,input().split())) # input
d = [0] * (N+1) # for memoization
cmp = [-1000000001] # 이진탐색을 위해 생성.
maxVal = 0 #최대값을 저장할 변수

for i in range(1, N+1): #arr 반복 실행.
    if cmp[-1] < arr[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
        cmp.append(arr[i])
        d[i] = len(cmp) - 1
        maxVal = d[i]
    else:
        d[i] = bisect_left(cmp, arr[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
        cmp[d[i]] = arr[i] #cmp 업데이트.
print(maxVal) #최대 길이 출력

res = []
for i in range(N, 0, -1):
    if d[i] == maxVal:
        res.append(arr[i])
        maxVal -= 1
res.reverse()
print(*res)
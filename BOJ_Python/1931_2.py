import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list()

for _ in range(n):
    start, finish = map(int, input().split())
    arr.append((start, finish))

arr = sorted(arr, key= lambda time : time[0])
arr = sorted(arr, key= lambda time : time[1])

cnt = 0
tmp = -123456789

for i in range(n):
    if arr[i][0] >= tmp:
        tmp = arr[i][1]
        cnt += 1
print(cnt)
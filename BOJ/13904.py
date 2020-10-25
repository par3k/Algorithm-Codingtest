# 과제
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
ans, day = 0, 0

arr = list()
for i in range(n):
    work = list(map(int, input().split()))
    if work[0] > day: day = work[0]
    work.append(i)
    arr.append(work)
arr = sorted(arr, key= lambda x : x[1], reverse=True)

tmp = [-1 for _ in range(day+1)]

for i in arr:
    for j in range(i[0], 0, -1):
        if tmp[j] == -1:
            tmp[j] = i[2]
            ans += i[1]
            break

print(ans)
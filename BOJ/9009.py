# 피보나치
import sys
input = lambda : sys.stdin.readline().rstrip()

arr = [1, 2]
for i in range(2, 44):
    arr.append(arr[i-2] + arr[i-1])

for _ in range(int(input())):
    n = int(input())
    ans = list()
    while n:
        for j in range(44):
            if arr[j] <= n:
                tmp = arr[j]
        n -= tmp
        ans.append(tmp)
        ans.sort()

    for k in range(len(ans)):
        print(ans[k], end=' ')
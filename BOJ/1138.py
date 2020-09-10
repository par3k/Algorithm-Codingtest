# 한 줄로 서기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))
ans = [0] * n

for i in range(1, n+1):
    num = arr[i-1]
    cnt = 0
    for j in range(n):
        if ans[j] == 0 and cnt == num:
            ans[j] = i
            break

        if ans[j] == 0:
            cnt += 1

print(*ans)
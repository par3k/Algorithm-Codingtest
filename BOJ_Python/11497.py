# 통나무 건너뛰기
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    # print(arr)
    ans, front, rear = 0, 0, n-1
    woods_arr = [0] * n

    for i in range(n):
        if i % 2 == 0:
            woods_arr[rear] = arr[i]
            rear -= 1
        else:
            woods_arr[front] = arr[i]
            front += 1
    # print(woods_arr)
    for i in range(1, n):
        ans = max(ans, abs(woods_arr[i] - woods_arr[i-1]))

    print(ans)
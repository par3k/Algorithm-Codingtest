# 통나무

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    front = 0
    back = n - 1
    tmp_arr = [0] * n

    for i in range(n):
        if i % 2 == 0:
            tmp_arr[front] = arr[i]
            front += 1
        else:
            tmp_arr[back] = arr[i]
            back -= 1

    ans = -999999999999

    for i in range(n - 1):
        ans = max(abs(tmp_arr[i + 1] - tmp_arr[i]), ans)

    print(ans)
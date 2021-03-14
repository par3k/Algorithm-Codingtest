import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
res = 0


def check(arr):
    cnt = 0

    for i in range(n):
        cnt_row, cnt_col = 1, 1
        for j in range(n - 1):
            if arr[i][j] == arr[i][j + 1]:
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1

            if arr[j][i] == arr[j + 1][i]:
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt = max(cnt, cnt_col, cnt_row)
    return cnt


for i in range(n):
    for j in range(n - 1):
        if arr[i][j] != arr[i][j + 1]: # row
            tmp = arr[i][j]
            arr[i][j] = arr[i][j + 1]
            arr[i][j + 1] = tmp

            res = max(res, check(arr))

            tmp = arr[i][j]
            arr[i][j] = arr[i][j + 1]
            arr[i][j + 1] = tmp

        if arr[j][i] != arr[j + 1][i]: # col
            tmp = arr[j][i]
            arr[j][i] = arr[j + 1][i]
            arr[j + 1][i] = tmp

            res = max(res, check(arr))

            tmp = arr[j][i]
            arr[j][i] = arr[j + 1][i]
            arr[j + 1][i] = tmp

print(res)
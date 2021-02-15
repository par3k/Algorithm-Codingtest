# 누울 자리를 찾아라
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr2 = [list(input()) for _ in range(n)]
row_ans, col_ans = 0, 0


def find_row(arr):
    cnt, row_cnt = 0, 0

    for i in arr:
        if i == '.':
            cnt += 1
        else:
            if cnt >= 2:
                row_cnt += 1
                cnt = 0
            else:
                cnt = 0

    if cnt >= 2:
        return row_cnt + 1
    else:
        return row_cnt


def find_col(arr):
    col_cnt = 0
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[j][i] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    col_cnt += 1
                    cnt = 0
                else:
                    cnt = 0

        if cnt >= 2:
            col_cnt += 1
    return col_cnt


for i in range(n):
    row_ans += find_row(arr2[i])
col_ans = find_col(arr2)

print(row_ans, col_ans)
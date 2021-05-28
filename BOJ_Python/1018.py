# 체스판 다시 칠하기
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

min_num = None

for i in range(n-7):
    for j in range(m-7):
        num1, num2 = 0, 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b-i-j) % 2 == 0:
                    if arr[a][b] == 'B':
                        num1 += 1
                else:
                    if arr[a][b] == 'W':
                        num1 += 1

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b-i-j) % 2 == 0:
                    if arr[a][b] == 'W':
                        num2 += 1

                else:
                    if arr[a][b] == 'B':
                        num2 += 1

        change = num1 if num1 < num2 else num2
        if min_num is None:
            min_num = change

        else:
            min_num = change if min_num > change else min_num

print(min_num)
# 괄호
import sys
input = lambda : sys.stdin.readline().rstrip()


def check(arr):
    tmp = []

    for i in range(len(arr)):
        if arr[i] == '(':
            tmp.append(arr[i])
        else:
            if len(tmp) == 0:
                print('NO')
                return
            else:
                tmp.pop()

    if len(tmp) == 0:
        print('YES')
        return
    else:
        print('NO')
        return


for _ in range(int(input())): check(input())
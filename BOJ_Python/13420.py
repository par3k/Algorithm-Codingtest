# 사칙연산
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr = list(input().split())

    if arr[1] == '+':
        if int(arr[0]) + int(arr[2]) == int(arr[4]):
            print('correct')
        else:
            print('wrong answer')

    elif arr[1] == '-':
        if int(arr[0]) - int(arr[2]) == int(arr[4]):
            print('correct')
        else:
            print('wrong answer')

    elif arr[1] == '*':
        if int(arr[0]) * int(arr[2]) == int(arr[4]):
            print('correct')
        else:
            print('wrong answer')

    elif arr[1] == '/':
        if int(arr[0]) / int(arr[2]) == int(arr[4]):
            print('correct')
        else:
            print('wrong answer')
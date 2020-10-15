# 균형잡힌 세상
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    data = input()
    if data == '.': break

    arr = list()
    tmp = True

    for i in data:
        if i == '(' or i == '[':
            arr.append(i)
        elif i == ')':
            if len(arr) == 0 or arr[-1] == '[':
                tmp = False
                break
            elif arr[-1] == '(':
                arr.pop()
        elif i == ']':
            if len(arr) == 0 or arr[-1] == '(':
                tmp = False
                break
            elif arr[-1] == '[':
                arr.pop()

    if tmp == True and len(arr) == 0: print('yes')
    else: print('no')
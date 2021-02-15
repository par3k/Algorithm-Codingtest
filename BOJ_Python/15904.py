# UCPC는 무엇의 약자일까?
import sys
input = lambda : sys.stdin.readline().rstrip()

arr = input()
check_list = ['U', 'C', 'P', 'C']
check = True

for i in range(len(check_list)):
    if check_list[i] in arr:
        check = True
        idx = arr.find(check_list[i])
        arr = arr[idx + 1:]
    else:
        check = False
        break

if check:
    print('I love UCPC')
else:
    print('I hate UCPC')
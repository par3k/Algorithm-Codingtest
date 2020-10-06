# 안정적인 문자열
import sys
input = lambda : sys.stdin.readline().rstrip()

for count in range(int(1e9)):
    arr = list(input())
    tmp = list()

    if arr.count('-'):
        break

    ans = 0
    for i in range(len(arr)):
        if len(tmp) == 0 and arr[i] == '}':
            ans += 1
            arr[i] = '{'
            tmp.append(arr[i])
        elif len(tmp) != 0 and arr[i] == '}':
            tmp.pop()
        else:
            tmp.append(arr[i])

    ans = ans + len(tmp) / 2
    print(f'{count+1}. {int(ans)}')

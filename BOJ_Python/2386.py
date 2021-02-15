# 도비의 영어 공부
import sys

while True:
    s = sys.stdin.readline().rstrip().lower()
    if s[0] == '#': break
    arr = list(s[2:])

    cnt = 0
    for i in range(len(arr)):
        if s[0] == arr[i]:
            cnt += 1

    print(f'{s[0]} {cnt}')
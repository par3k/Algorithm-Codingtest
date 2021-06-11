# 숫자 더하기
import sys

def make_sentence(arr):
    tmp, tmp2 = '', ''
    for i in range(len(arr)):
        if i % 2 == 0:
            tmp += str(arr[i])
        else:
            tmp2 += str(arr[i])

    print(int(tmp) + int(tmp2))

while True:
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    if s[0] == 0: break
    arr = []
    zero_cnt = 0

    for i in range(1, len(s)):
        if s[i] == 0: zero_cnt += 1
        arr.append(s[i])
    arr.sort()

    arr2 = []
    if zero_cnt > 0: # 0을 안에 넣어줘야 함
        for i in range(zero_cnt, zero_cnt + 2):
            arr2.append(arr[i])
        for i in range(zero_cnt):
            arr2.append(arr[i])
        for i in range(zero_cnt + 2, len(arr)):
            arr2.append(arr[i])
        make_sentence(arr2)
    else:
        make_sentence(arr)

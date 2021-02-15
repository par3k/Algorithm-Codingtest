# 문자가 몇갤까
import sys

while True:
    s = list(map(str, set(sys.stdin.readline().rstrip().lower())))
    if s == ['#']: break
    s.sort()

    arr = [0] * 26

    for i in s:
        if ord(i) - ord('a') >= 0:
            arr[ord(i) - ord('a')] += 1

    print(arr.count(1))
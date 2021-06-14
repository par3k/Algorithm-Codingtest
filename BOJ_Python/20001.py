# 고무오리 디버깅
import sys
arr = []

while True:
    s = sys.stdin.readline().rstrip()
    if s == "고무오리 디버깅 끝":
        if len(arr) == 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break
    elif s == "문제":
        arr.append(1)
    elif s == "고무오리":
        if len(arr) == 0:
            for _ in range(2):
                arr.append(1)
        else:
            arr.pop()
# 학점계산
import sys
input = lambda :sys.stdin.readline().rstrip()

arr = dict()
for _ in range(int(input())):
    s = input()
    if s in arr:
        arr[s] += 1
    else:
        arr[s] = 1

arr = sorted(arr.items(), key = lambda x: (-x[1], x[0]))
print(arr[0][0])
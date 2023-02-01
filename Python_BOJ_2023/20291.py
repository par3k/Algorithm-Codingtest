# 파일 정리

n = int(input())
tmp = list()
for _ in range(n):
    name, val = map(str, input().split("."))
    tmp.append(val)
arr = {}
for val in tmp:
    if val in arr:
        arr[val] += 1
    else:
        arr[val] = 1

arr = sorted(arr.items())
for key, val in arr:
    print(key, val)
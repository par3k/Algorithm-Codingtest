# 배열 합치기
a, b = map(int, input().split())

tmp = [list(map(int, input().split())) for _ in range(2)]

arr = list()
for i in range(a):
    arr.append(tmp[0][i])
for j in range(b):
    arr.append(tmp[1][j])

arr.sort()
for i in range(len(arr)):
    print(arr[i], end = ' ')
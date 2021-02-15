# 나이순 정렬

N = int(input())

arr = []

for i in range(N):
    input_data = input().split()
    arr.append((int(input_data[0]), input_data[1]))

arr = sorted(arr, key=lambda student: student[0])

for i in arr:
    print(*i)
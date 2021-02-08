# 자석 체인

n = int(input())
arr = input()

cnt = 0
for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        cnt = 1
        print("No")
        exit()

if cnt == 0:
    print("Yes")
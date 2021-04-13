arr = [int(input()) for _ in range(9)]

sum = sum(arr)
flag = False

for i in range(9):
    for j in range(i + 1, 9):
        if sum - arr[i] - arr[j] == 100:
            if not flag:
                arr[i] = 0
                arr[j] = 0
                flag = True

arr = sorted(arr)
for i in arr:
    if i == 0 : continue
    print(i)
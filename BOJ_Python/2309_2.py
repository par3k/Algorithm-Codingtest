arr = [0] * 9
for i in range(len(arr)):
    arr[i] = int(input())

sum_height = sum(arr)

flag = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if not flag:
            if sum_height - arr[i] - arr[j] == 100:
                arr[i] = 0
                arr[j] = 0
                flag = True

arr = sorted(arr)
for i in arr:
    if i == 0:
        continue
    else:
        print(i)
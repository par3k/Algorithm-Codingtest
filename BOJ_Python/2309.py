import sys

arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
arr.sort()
sum = sum(arr)

for i in range(9):
    for j in range(i+1, 9):
        if (sum - arr[i] - arr[j]) == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                else:
                    print(arr[k])
            exit(0)
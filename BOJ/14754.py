# Pizza Boxes
import sys
input = lambda : sys.stdin.readline().rstrip()

x, y = map(int, input().split())

arr = []
arr2 = set()

for i in range(x):
    row = list(map(int, input().split()))
    arr2.add(max(row))
    arr.append(row)

for j in range(y):
    arr2.add(max(arr[i][j] for i in range(x)))

print(sum(map(sum, arr)) - sum(arr2))
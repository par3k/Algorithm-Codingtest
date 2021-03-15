import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = [[0] * 2 for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    arr[i][0], arr[i][1] = x, y

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
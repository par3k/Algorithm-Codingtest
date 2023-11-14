n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    
    tmp = arr[i-1 : j]
    tmp = tmp[::-1]
    arr[i-1:j] = tmp

for i in arr:
    print(i, end=' ')
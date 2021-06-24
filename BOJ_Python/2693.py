# N번째 큰 수

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[2])
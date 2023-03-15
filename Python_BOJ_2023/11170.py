# 0의 개수

for _ in range(int(input())):
    n, m = map(int, input().split())

    cnt = 0
    for i in range(n, m + 1):
        arr = list(map(str, str(i)))
        
        for j in range(len(arr)):
            if arr[j] == '0':
                cnt += 1
    print(cnt)
# 소수 찾기

N = int(input())
num = list(map(int, input().split()))

cnt = 0
count = 0

for i in num:
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        count += 1
    cnt = 0

print(count)
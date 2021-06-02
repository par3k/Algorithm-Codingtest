# 소수
M = int(input())
N = int(input())

cnt = 0
numbers = []

for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1

    if cnt == 2:
        numbers.append(i)
    cnt = 0

if numbers == []:
    print('-1')
else:
    print(sum(numbers))
    print(min(numbers))
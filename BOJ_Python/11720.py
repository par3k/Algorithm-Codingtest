# 숫자의 합

n = int(input())
numbers = list(map(int,input()))

sum = 0

for i in range(n):
    sum = sum + numbers[i]

print(sum)
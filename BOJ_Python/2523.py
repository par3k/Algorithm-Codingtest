# 별 찍기 - 13

n = int(input())

for i in range(1,n+1):
    print('*' * i)
for j in range(1,n):
    print('*' * (n-j))

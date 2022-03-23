# 완전제곱수
m = int(input())
n = int(input())

lis = []

for i in range(m, n + 1):
    sqrt = i ** (1/2)
    if sqrt % 1 == 0:
        lis.append(i)

if len(lis):
    print(sum(lis))
    print(min(lis))
else:
    print(-1)
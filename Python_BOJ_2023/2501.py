# 약수 구하기

n, k = map(int, input().split())

yaksu = list()
for i in range(1, n + 1):
    if n % i == 0:
        yaksu.append(i)

if k > len(yaksu):
    print(0)
else:
    print(yaksu[k - 1])
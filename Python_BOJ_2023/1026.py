# 보물

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
arr2 = list(map(int, input().split()))
arr2.sort(reverse=True)

sum = 0

for i in range(n):
    tmp = arr1[i] * arr2[i]
    sum += tmp
print(sum)
# 숫자 카드2

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

answer = dict()

for i in arr1:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for i in arr2:
    if i in answer:
        print(answer[i], end=' ')
    else:
        print(0, end=' ')
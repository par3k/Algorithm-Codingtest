# 숫자 카드2

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
list = list(map(int, input().split()))

ans = {}

for i in cards:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1

for j in list:
    if j in ans:
        print(ans[j], end=' ')
    else:
        print(0, end=' ')
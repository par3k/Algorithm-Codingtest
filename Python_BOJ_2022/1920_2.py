# 수찾기

n = int(input())
list_1 = set(map(int, input().split()))
m = int(input())
list_2 = list(map(int, input().split()))

for i in list_2:
    print(1 if i in list_1 else 0)
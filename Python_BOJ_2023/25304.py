# 영수증

tot = int(input())
ssum = 0
for _ in range(int(input())):
    price, val = map(int, input().split())
    ssum += price * val

if tot == ssum:
    print("Yes")
else:
    print("No")
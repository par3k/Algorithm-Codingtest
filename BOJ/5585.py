# 거스름돈
from sys import stdin

money = 1000 - int(stdin.readline().rstrip())
pouch = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in pouch:
    cnt += money // i
    money %= i

print(cnt)
# 거스름돈
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
coin = 0

while True:
    if n % 5 != 0:
        n -= 2
        coin += 1

    else:
        coin += n / 5
        n = n % 5

    if n == 0:
        print(int(coin))
        break

    elif n < 0:
        print(-1)
        break
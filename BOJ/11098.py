# 첼시를 도와줘
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    max_price, max_name = 0, ''

    for i in range(int(input())):
        price, name = input().split()
        price = int(price)

        if price > max_price:
            max_price = price
            max_name = name

    print(max_name)
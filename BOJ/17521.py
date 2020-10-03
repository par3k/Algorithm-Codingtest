# Byte Coin
import sys
input = lambda : sys.stdin.readline().rstrip()

n, W = map(int, input().split())
coin_prices = [0] * 20

for i in range(0, n):
    coin_prices[i] = int(input())

for i in range(n-1):
    if coin_prices[i] < coin_prices[i+1]:
        x = W // coin_prices[i] # 바꾼 동전 갯수
        W = W % coin_prices[i] # 동전을 바꾼 후 남은 잔돈
        x = coin_prices[i+1] * x # 코인 가격 상승으로 생긴 이득
        W += x # 현재 잔고

    else:
        continue
print(W)
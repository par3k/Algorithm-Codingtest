# 주유소
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
ans = 0

for i in range(n-1):
    min_price = min(price[i], min_price)
    ans += dis[i] * min_price

print(ans)
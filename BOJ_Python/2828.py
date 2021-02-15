# 사과 담기 게임
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
j = int(input())
apples = [int(input()) for _ in range(j)]

basket_size = m - 1
basket_left = 1
basket_right = basket_left + basket_size
ans = 0

for i in apples:
    if basket_left <= i <= basket_right:
        continue

    if i < basket_left:
        ans += abs(basket_left - i)
        basket_left = i
        basket_right = i + basket_size

    elif i > basket_right:
        ans += abs(i - basket_right)
        basket_left = i - basket_size
        basket_right = i

print(ans)
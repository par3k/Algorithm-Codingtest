# 카드 합체 놀이
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int,input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    new_num = cards[0] + cards[1]
    cards[0], cards[1] = new_num, new_num

ans = sum(cards)
print(ans)
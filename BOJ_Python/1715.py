# 카드 정렬하기
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

cards = []

n = int(input())
for _ in range(n):
    heapq.heappush(cards, int(input()))

if n == 1:
    print(0)
else:
    sum = 0
    while len(cards) > 1:
        tmp = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, tmp)
        sum += tmp

    print(sum)

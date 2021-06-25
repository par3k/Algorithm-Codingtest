# 카드
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
cards = deque(i + 1 for i in range(N))

ans = []
while len(cards) > 1:
    ans.append(cards.popleft())
    cards.rotate(-1)
ans.append(cards[0])
print(' '.join(map(str, ans)))
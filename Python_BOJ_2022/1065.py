# 블랙잭
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# n장의 카드 중 3장을 골라 m과 최대한 가까운 수를 만들기
tmp = 0
ans = -9990
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp <= m:
                ans = max(ans, tmp)

print(ans)
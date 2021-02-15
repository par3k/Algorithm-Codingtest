# 동전 0

N, K = map(int, input().split())

pouch = []
cnt = 0

for _ in range(N):
    coin = int(input())
    pouch.append(coin)

pouch.sort(reverse=True)

for i in pouch:
    cnt += K // i
    K = K % i

print(cnt)
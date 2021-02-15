# 블랙잭

N, M = map(int, input().split())
Cards = list(map(int, input().split()))

ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = Cards[i] + Cards[j] + Cards[k]

            if total <= M:
                ans = max(total, ans)
                
print(ans)

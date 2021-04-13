n, m = map(int,input().split())
card = list(map(int, input().split()))
ans = -123456789

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp = card[i] + card[j] + card[k]
            if tmp <= m:
                ans = max(ans, tmp)
print(ans)

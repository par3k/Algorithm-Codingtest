# 설탕 배달

n = int(input())
ans = 0

while 1:
    if n % 5 == 0:
        ans = ans + (n//5)
        print(ans)
        break
    n = n - 3
    ans += 1
    if n < 0:
        print(-1)
        break
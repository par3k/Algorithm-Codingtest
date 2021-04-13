a, b = map(int, input().split())
ans = 0
while True:
    if a == b:
        ans += 1
        break

    if b < a:
        ans = -1
        break

    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        ans = -1
        break

    ans += 1
print(ans)
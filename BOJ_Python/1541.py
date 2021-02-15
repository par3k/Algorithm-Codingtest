# 잃어버린 괄호

num = list(map(str, input().split('-')))

if '+' in num[0]:
    arr = list(map(int, num[0].split('+')))
    ans = sum(arr)
else:
    ans = int(num[0])

for i in range(1, len(num)):
    if '+' in num[i]:
        arr = list(map(int, num[i].split('+')))
        ans -= sum(arr)
    else:
        ans -= int(num[i])

print(ans)

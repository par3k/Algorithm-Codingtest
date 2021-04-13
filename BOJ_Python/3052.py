arr = [int(input()) for _ in range(10)]
num = [0] * 42

for i in range(10):
    num[arr[i] % 42] += 1

ans = 0
for i in num:
    if i != 0:
        ans += 1
print(ans)
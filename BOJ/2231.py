# 분해합

n = int(input())
ans = []

for i in range(1, n+1):
    if n == i + sum(map(int, str(i))):
        ans.append(i)
        
if len(ans) == 0:
    print('0')
else:
    print(min(ans))



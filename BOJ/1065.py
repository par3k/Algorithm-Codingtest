# 한수

ans = 0

def Hansu(x):
    global ans
    if x//100 - x%100 //10 is x%100 // 10 - x%10:
        ans += 1
    return ans

a = int(input())

for i in range(1, a+1):
    if i < 100:
        ans += 1
    else:
        Hansu(i)

print(ans)


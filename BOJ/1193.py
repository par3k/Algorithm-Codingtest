# 분수찾기

x = int(input())

nums = 0
i = 0

while nums < x:
    i += 1
    nums += i

if i % 2 == 0:
    up = i + x - nums
    lo = 1 + nums - x

elif i % 2 != 0:
    up = 1 + nums - x
    lo = i + x - nums

print("%d/%d" %(up, lo))
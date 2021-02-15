# 분수 찾기

X = int(input())

nums = 0
i = 0
boonja = 0
boonmo = 0

while nums < X:
    i += 1
    nums = nums + i

if i % 2 == 0:
    boonja = i + X - nums
    boonmo = 1 + nums - X

elif i % 2 == 1:
    boonja = 1 + nums - X
    boonmo = i + X - nums


print(f'{boonja}/{boonmo}')



# 손익분기점

a, b, c = map(int,input().split())

# n = 1
# while 1:
#     if a + ( b * n) < c * n:
#         break
#     n += 1
# print(n)

if b == c or b > c:
    print(-1)
else:
    print(int(a/(c-b)+1))
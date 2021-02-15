# 직각삼각형

# import math
#
# while True:
#     a, b, c = list(map(int, input().split()))
#
#     if a == 0 and b == 0 and c == 0:
#         break
#     else:
#         if c == math.sqrt(a**2 + b**2):
#             print('right')
#         elif c != math.sqrt(a**2 + b**2):
#             print('wrong')

while True:
    a, b, c = map(int, input().split())
    line = []
    line.append(a)
    line.append(b)
    line.append(c)
    if a == 0 and b == 0 and c == 0:
        break
    else:
        maximum = max(line)
        line.remove(maximum)

        if pow(maximum, 2) == pow(line[0], 2) + pow(line[1], 2):
            print('right')
        else:
            print('wrong')

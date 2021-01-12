# 미국 스타일
import sys
input = lambda : sys.stdin.readline()

kg_tolb = 2.2046
lb_tokg = 0.4536
l_tog = 0.2642
g_tol = 3.7854

for _ in range(int(input())):
    a, b = map(str, input().split())
    if b == 'kg':
        a = float(a) * kg_tolb
        b = 'lb'
    elif b == 'lb':
        a = float(a) * lb_tokg
        b = 'kg'
    elif b == 'l':
        a = float(a) * l_tog
        b = 'g'
    else:
        a = float(a) * g_tol
        b = 'l'
    print('%.4f' %a, b)

# Equality

a, b = input().split('=')

if eval(a) == int(b):
    print('YES')
else:
    print('NO')
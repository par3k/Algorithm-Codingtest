n = int(input())

for i in range(1, 2 * n + 1):
    if i % 2 != 0:
        print('*' + ((n-1)//2 * (" "+"*")))
    else:
        print(' '+ (n//2) * ("*"+" "))
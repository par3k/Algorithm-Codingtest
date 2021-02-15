# 상근이의 체스판

r, c = map(int, input().split())
a, b = map(int, input().split())

for i in range(r):
    for _ in range(a):
        for j in range(c):
            print('.' * b if (i + j) % 2 else 'X' * b, end='')
        print()
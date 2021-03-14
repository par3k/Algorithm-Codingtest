import sys
input = lambda :sys.stdin.readline().rstrip()

r, b = map(int, input().split())

for i in range(3, 2000):
    for j in range(3, i + 1):
        tmp = (i * 2) + (j - 2) * 2
        if r == tmp and b == (i * j) - tmp:
            print(i, j)
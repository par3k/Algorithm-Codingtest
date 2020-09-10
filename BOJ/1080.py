# 행렬
import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

cnt = 0

'''
0000
0010
0000

1110
1100
1110

1001
1011
1001

'''

def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False

    return True


def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1- A[i][j]


for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            change(i, j)

if check():
    print(cnt)
else:
    print(-1)
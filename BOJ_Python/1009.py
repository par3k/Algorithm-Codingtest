# 분산 처리
import sys
input = lambda :sys.stdin.readline().rstrip()

list = [[],
        [1],
        [6, 2, 4, 8],
        [1, 3, 9, 7],
        [6, 4],
        [5],
        [6],
        [1, 7, 9, 3],
        [6, 8, 4, 2],
        [1, 9]]
ans = []

for _ in range(int(input())):
    a, b = map(int ,input().split())
    a = int(str(a)[-1])
    if a != 0:
        print(list[a][b % len(list[a])])
    else:
        print(10)
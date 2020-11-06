# 전화번호 목록
import sys
input = lambda : sys.stdin.readline().rstrip()


def check():
    for i in range(len(num) - 1):
        if num[i] == num[i + 1][0: len(num[i])]:
            print('NO')
            return
    print('YES')


for _ in range(int(input())):
    n = int(input())
    num = [list(map(int, input())) for _ in range(n)]
    num.sort()
    check()
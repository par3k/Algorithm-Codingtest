# 전구와 스위치
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
first = list(map(int,input()))
second = list(map(int, input()))
ans = -1

'''
000
110
001
010
'''


def switch(start):
    global first, ans

    tmp = first[:]
    cnt = 0

    for i in range(start, n):
        if not (0 < i and tmp[i - 1] == second[i - 1]):
            cnt += 1

            if 0 < i:
                tmp[i - 1] = 1 if tmp[i - 1] == 0 else 0

            if i < n-1:
                tmp[i + 1] = 1 if tmp[i + 1] == 0 else 0
            tmp[i] = 1 if tmp[i] == 0 else 0

        if i == n-1 and tmp == second:
            ans = cnt if ans == -1 else min(ans, cnt)
            break

switch(0)
switch(1)

print(ans)
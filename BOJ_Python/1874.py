# 스택 수열
import sys
input = lambda : sys.stdin.readline().rstrip()

stack = list()
ans = list()
cnt = 1
tmp = True

for _ in range(int(input())):
    n = int(input())

    while cnt <= n:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if stack[-1] == n:
        stack.pop()
        ans.append('-')
    else:
        tmp = False

if tmp == False:
    print('NO')
else:
    for i in ans:
        print(i)
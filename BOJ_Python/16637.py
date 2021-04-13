# 괄호 추가하기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
num, op = list(), list()
ans = -123456789


def dfs(idx, sub_tot):
    global ans
    if idx == len(op):
        ans = max(ans, int(sub_tot))
        return

    first = str(eval(sub_tot + op[idx] + num[idx+ 1])) # (3+8)*7-9*2
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        second = str(eval(num[idx + 1] + op[idx + 1] + num[idx + 2])) # 3+(8*7)-9*2
        second = str(eval(sub_tot + op[idx] + second))
        dfs(idx + 2, second)


for e in input():
    num.append(e) if e.isdigit() else op.append(e)

dfs(0, num[0])
print(ans)
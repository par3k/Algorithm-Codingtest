# 쇠막대기
import sys
input = lambda : sys.stdin.readline().rstrip()
q = list(input())

ans = 0
stack = []

for i in range(len(q)):
    if q[i] == '(':
        stack.append(q[i])

    else:
        if q[i - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)
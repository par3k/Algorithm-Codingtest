# 괄호 끼워넣기
import sys

s = sys.stdin.readline().rstrip()
ans = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else:
            ans += 1

ans += len(stack)
print(ans)
# 압축
import sys
input = lambda :sys.stdin.readline().rstrip()

s = input()
stack = []

for i in range(len(s)):
    if i < len(s) - 1 and s[i + 1] == '(':
        stack.append(s[i])
    elif s[i] == '(':
        stack.append('(')
    elif s[i] == ')':
        cnt = 0
        while True:
            tmp = stack.pop()
            if tmp == '(': break
            cnt += tmp
        stack.append(int(stack.pop()) * cnt)
    else:
        stack.append(1)

print(sum(stack))
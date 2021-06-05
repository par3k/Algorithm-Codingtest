# 후위 표기식 2
import sys
input = lambda :sys.stdin.readline().rstrip()

operator = '*+/-'

n = int(input())
s = input()

num = []
num_stack = []

for _ in range(n):
    num.append(int(input()))

for c in s:
    if c in operator:
        tmp1 = num_stack.pop()
        tmp2 = num_stack.pop()

        if c == '*':
            ans = tmp1 * tmp2
        elif c == '+':
            ans = tmp1 + tmp2
        elif c == '/':
            ans = tmp2 / tmp1
        elif c == '-':
            ans = tmp2 - tmp1

        num_stack.append(ans)
    else:
        num_stack.append(num[ord(c) - ord('A')])
        print(num_stack)

print('%0.2f' %num_stack[-1])
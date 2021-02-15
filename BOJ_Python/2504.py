# 괄호의 값
import sys
input = lambda : sys.stdin.readline().rstrip()
data = input().strip()


def check(a):
    stack = []
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
            print(stack)
        elif i == ')' and stack:
            if stack[-1] == '(':
                stack = stack[:-1]
                print(stack)
            else:
                stack.append(i)
                print(stack)
        elif i == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
                print(stack)
            else:
                stack.append(i)
                print(stack)
        else:
            stack.append(i)
            print(stack)

    if stack:
        return False
    else:
        return True


def solve(b):
    stack = []
    for j in b:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) -1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
        elif j == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) -1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    return sum(stack)


if not check(data):
    print(0)
else:
    print(solve(data))


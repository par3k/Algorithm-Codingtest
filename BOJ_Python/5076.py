# Web Pages
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '#': break
    stack = []
    flag = False
    tmp = ''

    for i in range(len(s)):
        if s[i] == '<':
            flag = True
        elif s[i] == '>':
            flag = False
            if tmp and tmp[-1] == '/':
                tmp = ''
                continue
            elif stack and stack[-1] == tmp[1:]:
                stack.pop()
            else:
                stack.append(tmp)
            tmp = ''

        if flag and s[i] == ' ' and s[i + 1] != '/':
            flag = False

        if flag and s[i] != '<':
            tmp += s[i]

    if stack:
        print("illegal")
    else:
        print("legal")
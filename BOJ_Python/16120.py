# PPAP
import sys

s = sys.stdin.readline().rstrip().upper()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if len(stack) >= 4:
        if stack[-4:] == ["P", "P", "A", "P"]:
            for _ in range(4):
                stack.pop()
            stack.append('P')

if stack == ["P", "P", "A", "P"] or stack == ['P']:
    print("PPAP")
else:
    print("NP")
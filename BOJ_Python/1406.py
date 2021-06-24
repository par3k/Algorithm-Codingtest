# 에디터
import sys
input = lambda :sys.stdin.readline().rstrip()

left = list(input())
right = []

T = int(input())
while T:
    T -= 1
    cmd = input()
    if cmd[0] == 'L':
        if len(left):
            right.append(left.pop())
    elif cmd[0] == 'D':
        if len(right):
            left.append(right.pop())
    elif cmd[0] == 'B':
        if len(left):
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])

ans = left
while len(right):
    ans.append(right.pop())

print(''.join(ans))
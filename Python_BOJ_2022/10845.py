# 큐
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

queue = deque()
for _ in range(int(input())):
    cmd = list(input().split())
    
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)

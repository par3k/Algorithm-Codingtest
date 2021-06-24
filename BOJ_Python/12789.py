# 도키도키 간식드라마
from collections import deque
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
queue = deque(map(int, input().split()))
stack = deque()
target = 1

while queue:
    if queue and queue[0] == target:
        queue.popleft()
        target += 1
    else:
        stack.append(queue.popleft())

    while stack and stack[-1] == target:
        stack.pop()
        target += 1

print("Nice" if not stack else "Sad")

    # if len(arr) != 0 and len(tmp) == 0:
    #     if arr[0] == target:
    #         arr.popleft()
    #         target += 1
    #     else:
    #         tmp.append(arr.popleft())
    # elif len(arr) == 0 and len(tmp) != 0:
    #     if tmp[-1] == target:
    #         tmp.pop()
    #         target += 1
    #     else:
    #         arr.append(tmp.pop())
    # elif len(arr) != 0 and len(tmp) != 0:
    #     if arr[0] == target:
    #         arr.popleft()
    #         target += 1
    #     elif tmp[-1] == target:
    #         tmp.pop()
    #         target += 1
    #     else:
    #         tmp.append(arr.popleft())
    # else:
    #     Flag = True
    #     break

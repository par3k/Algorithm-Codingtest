# 카드2
from collections import deque

n = int(input())
list = deque()
for i in range(1, n + 1):
    list.append(i)

while True:
    if len(list) == 1:
        print(list.pop())
        break
    list.popleft()
    top = list.popleft()
    list.append(top)
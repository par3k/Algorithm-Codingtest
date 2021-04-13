import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr, num = map(str, input().split())
    a = deque(arr)
    tmp = list()
    for i in range(int(num)):
        tmp.append(a.pop())
        a.appendleft(tmp.pop())

    print(f"Shifting {arr} by {num} positions gives us: {''.join(a)}")



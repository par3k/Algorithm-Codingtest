# 톱니바퀴
from collections import deque

wheels = [deque(map(int, input())) for _ in range(4)]
print(wheels)

def cw(num, dir):
    global wheels
    if num == 4:
        return
    if wheels[num - 1][2] != wheels[num][6]:
        cw(num + 1, -dir)
        wheels[num].rotate(dir)
    else:
        return

def ccw(num, dir):
    global wheels
    if num == -1:
        return
    if wheels[num + 1][6] != wheels[num][2]:
        ccw(num - 1, -dir)
        wheels[num].rotate(dir)
    else:
        return

ans = 0
for _ in range(int(input())):
    wheel, dir = map(int, input().split())
    cw(wheel, -dir)
    ccw(wheel - 2, -dir)
    wheels[wheel - 1].rotate(dir)

for i in range(4):
    ans += (2 ** i) * wheels[i][0]

print(ans)

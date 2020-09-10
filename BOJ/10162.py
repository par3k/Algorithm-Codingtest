# 전자레인지
import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

buttons = [300, 60, 10]
cnt = [0, 0, 0]

for i in range(len(buttons)):
    cnt[i] += t // buttons[i]
    t %= buttons[i]

if t % buttons[i] != 0:
    print(-1)

else:
    print(f'{cnt[0]} {cnt[1]} {cnt[2]}')
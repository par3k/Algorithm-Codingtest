# 농구 경기
import sys
from collections import Counter
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
player, fn, cnt = list(), list(), 0

for i in range(n):
    a = input()
    player.append(a[0])
player_cnt = Counter(player)

for i, j in player_cnt.items():
    if j >= 5:
        fn.append(i)
        cnt += 1

fn.sort()
if cnt == 0:
    print('PREDAJA')
else:
    print(''.join(fn))
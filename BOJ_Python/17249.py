# 태보태보 총난타
import sys
n = sys.stdin.readline().rstrip()
l_cnt, r_cnt, start = 0, 0, 0

for i in range(start, len(n)):
    if n[i] == '@':
        l_cnt += 1
    elif n[i] == '0':
        start = i
        break

for j in range(start, len(n)):
    if n[j] == '@':
        r_cnt += 1

print(f'{l_cnt} {r_cnt}')
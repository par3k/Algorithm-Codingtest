# 아파트 임대 (실패)
import sys
input = sys.stdin.readline

r = 0
for _ in range(int(input())):
    s = int(input())
    x, a = 1, False
    while s > x and 2 * x * (x + 1) < (1 << 31):
        if (s - x) % (x + x + 1) == 0:
            a = True
            break
        x += 1
    if not a: r += 1
print(r)
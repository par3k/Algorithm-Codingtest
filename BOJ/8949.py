# 대충 더해
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
ans = list()

while a or b:
    ans.append(str(a % 10 + b % 10))
    a //= 10
    b //= 10

print(''.join(ans[::-1]))
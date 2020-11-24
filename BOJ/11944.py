# NN
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
ans = str(n) * n

print(ans[:m])

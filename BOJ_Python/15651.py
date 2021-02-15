# N과 M(3)

from itertools import product
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

for n in product(range(1, n+1), repeat=m):
    print(*n)

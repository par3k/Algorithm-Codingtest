# N과 M(2)

from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

for n in combinations(range(1, n+1), m):
    print(*n)
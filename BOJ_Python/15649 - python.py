# N과 M(1)

from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

for n in permutations(range(1, n+1), m):
    print(*n)
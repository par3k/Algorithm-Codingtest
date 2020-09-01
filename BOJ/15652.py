# N과 M(4)

import itertools
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

for n in itertools.combinations_with_replacement(range(1, n+1), m):
    print(*n)
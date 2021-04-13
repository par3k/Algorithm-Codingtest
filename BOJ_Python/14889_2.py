import sys
from itertools import combinations
input = lambda :sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
tmp = [sum(i) + sum(j) for i, j in zip(graph, zip(*graph))]
all_stat = sum(tmp) // 2

print(min([abs(all_stat - sum(stat)) for stat in combinations(tmp, N // 2)]))

print(tmp)
for i, j in zip(graph, zip(*graph)):
    print(i, j)
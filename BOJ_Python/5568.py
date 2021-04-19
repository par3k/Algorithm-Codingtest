# 카드 놓기
import sys
from itertools import permutations
input = lambda :sys.stdin.readline().rstrip()

n, k = int(input()), int(input())
list = [input() for _ in range(n)]

answer = set()
for i in permutations(list, k):
    answer.add(''.join(i))

print(len(answer))
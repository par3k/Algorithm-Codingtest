# 순열
import sys
from itertools import permutations
input = lambda :sys.stdin.readline().rstrip()

while True:
    try:
        s, n = input().split()
    except:
        break

    answer = [0]
    for i in permutations(s, int(len(s))):
        answer.append(''.join(i))

    if len(answer) < int(n):
        print(f'{s} {n} = No permutation')
    else:
        print(f'{s} {n} = {answer[int(n)]}')
# 요세푸스 문제0
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
circle = [str(x) for x in range(1, N+1)]
p = 0
seq = []
while circle:
    p = (p + M - 1) % N
    seq.append(circle.pop(p))
    N -= 1

print('<', ', '.join(seq), ">", sep='')
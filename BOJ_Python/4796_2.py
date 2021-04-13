import sys
tc = 1
while True:
    L, P, V = map(int, sys.stdin.readline().rstrip().split())
    if L == P == V == 0 :break
    ans = L * (V // P) + min(L, V % P)
    print(f'Case {tc}: {ans}')
    tc += 1
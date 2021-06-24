# 프린터 큐
import sys
input = lambda :sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(n))
    idx[m] = 'tgt'
    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'tgt':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
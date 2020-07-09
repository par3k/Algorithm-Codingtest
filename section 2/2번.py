# K번째 작은 수

import sys
sys.stdin = open("../input.txt", "rt")

T = int(input())
count = 0

for i in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1: e]
    # print(a)
    a.sort()
    # print(a)
    print('#%d %d' %(i+1, a[k-1]))
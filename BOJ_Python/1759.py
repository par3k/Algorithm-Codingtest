import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

mo = ['a','e', 'i', 'o', 'u']
za = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']

l, c = map(int, input().split())
arr = list(input().split())
arr = sorted(arr)
tmp = list()

for i in combinations(arr, l):
    tmp.append(i)

ans = list()
for i in range(len(tmp)):
    ans.append(''.join(tmp[i]))

for i in range(len(ans)):
    cnt = 0
    for j in range(l):
        if ans[i][j] in za:
            cnt += 1
    if cnt < 2:
        ans[i] = ' '

for i in range(len(ans)):
    cnt = 0
    if ans[i] == ' ': continue
    for j in range(l):
        if ans[i][j] in mo:
            cnt += 1
    if cnt < 1:
        ans[i] = ' '


for i in range(len(ans)):
    if ans[i] == ' ': continue
    print(ans[i])

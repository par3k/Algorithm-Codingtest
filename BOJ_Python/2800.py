# 괄호 제거
from itertools import combinations
import sys

s = list(input())
print(s)

p, idx = [], []
for i, val in enumerate(s):
    if val == '(':
        s[i] = ''
        p += [i]
    if val == ')':
        s[i] = ''
        idx += [[p.pop(), i]]

print(p)
print(idx)
out = set()

for i in range(len(idx)):
    for j in combinations(idx, i):
        print(j)
        p = s[:]
        for v, w in j:
            p[v] = '('
            p[w] = ')'
        out.add(''.join(p))

for i in sorted(out):
    print(i)
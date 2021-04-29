# 연결 요소의 갯수
import sys
input = lambda : sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key=lambda x : min(x))

for i in arr:
    a, b = i
    if find(parent, a) != find(parent, b):
        union(a, b)

parent.pop(0)
print(len(set(parent)))
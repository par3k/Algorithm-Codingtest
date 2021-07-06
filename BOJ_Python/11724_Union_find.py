import sys
input = lambda :sys.stdin.readline().rstrip()

def getParent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b


def find(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a != b:
        union(parent, a, b)


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key = lambda x : min(x))

for i in arr:
    a, b = i
    find(parent, a, b)

parent.pop(0)
print(len(set(parent)))
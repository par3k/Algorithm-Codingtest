import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parent = [i for i in range(1, n + 1)]
graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key= lambda x : min(x))


def find(x):
    if parent[x] != x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in graph:
    a, b = i
    if find(a) != find(b):
        union(a, b)

parent.pop(0)
print(parent)
print(len(set(parent)))
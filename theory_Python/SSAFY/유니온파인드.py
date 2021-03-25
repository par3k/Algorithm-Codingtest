n = int(input())

parent = [0] * n # make set
for i in range(n):
    parent[i] = i
print(parent)

def find(x): # find set
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b): # union set
    a = find(a)
    b = find(b)
    if a == b: return False
    parent[b] = a
    return True


union(0, 1)
print(parent)
union(1, 2)
print(parent)
union(3, 4)
print(parent)
union(0, 2)
print(parent)
union(0, 4)
print(parent)
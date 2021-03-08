import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
parent = list()

for i in range(n + 1):
    parent.append(i)


def getParent(x):
    if x == parent[x]:
        return x
    else :
        parent[x] = getParent(parent[x])
    return parent[x]


def Union(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b: return
    if a < b: parent[b] = a
    else: parent[a] = b


for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        Union(b, c)
    else:
        if getParent(b) == getParent(c):
            print("YES")
        else:
            print("NO")
import sys
input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

edges.sort(key = lambda x : x[2])
parent = {}

for i in range(v):
    parent[i + 1] = i + 1


def find(x, arr):
    if x == arr[x]:
        return x
    arr[x] = find(arr[x], arr)
    return arr[x]


def union(x, y, arr):
    x = find(x, arr)
    y = find(y, arr)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y


def findParent(x, y, arr):
    x = find(x, arr)
    y = find(y, arr)
    if x == y: return True
    else: return False


MST = list()
for e in edges:
    f, t, w = e
    if not findParent(f, t, parent):
        union(f, t, parent)
        MST.append(e)

ans = 0
for i in range(len(MST)):
    ans += MST[i][2]
print(ans)
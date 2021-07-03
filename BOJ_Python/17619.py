# 개구리 점프
import sys
input = lambda :sys.stdin.readline().rstrip()

parent = [i for i in range(100001)]
n, q = map(int, input().split())

arr = [(-1, -1)]
for i in range(n):
    s, e, _ = map(int, input().split())
    arr.append((s, e, i + 1))

arr.sort()
cmd = [tuple(map(int, input().split())) for _ in range(q)]


def find(parent, x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(parent,x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def Solution():
    cs, ce, _ = arr[1]
    for i in range(2, len(arr)):
        ss, ee, _ = arr[i]
        if ce >= ss:
            ce = max(ce, ee)
            union(parent, arr[i - 1][2], arr[i][2])
        else:
            cs = ss
            ce = ee


Solution()
for i, j in cmd:
    arr[i] = find(parent, i)
    arr[j] = find(parent, j)
    print(1) if parent[i] == parent[j] else print(0)
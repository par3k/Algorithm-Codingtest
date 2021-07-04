# 집합의 표현
import sys
sys.setrecursionlimit(100001)
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]


def union(arr, a, b):
    a = find(a)
    b = find(b)
    if a == b: return
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(parent, b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")


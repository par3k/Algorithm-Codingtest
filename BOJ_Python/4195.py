# 친구 네트워크
import sys
input = lambda :sys.stdin.readline().rstrip()


def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]


for tc in range(int(input())):
    parent = dict()
    number = dict()
    f = int(input())

    for _ in range(f):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)

        print(number[find(x)])
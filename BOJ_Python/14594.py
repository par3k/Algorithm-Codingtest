# 동방 프로젝트 (Small)

n = int(input())
m = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

cnt = 0
for i in range(m):
    x, y = map(int, input().split())

    for j in range(x, y + 1):
        if find(j) != find(y):
            union(j, y)
            cnt += 1

print(n - cnt)
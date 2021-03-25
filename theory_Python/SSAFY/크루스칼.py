v, e = map(int, input().split())

edgeList = list()
ans = 0

for i in range(e):
    from_, to_, weight = map(int, input().split())
    edgeList.append((weight, from_, to_))

edgeList.sort() # weight 기준 정렬됨

parent = [0] * v # make set
for i in range(v):
    parent[i] = i


def find(x): # find set
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b): # union set
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for edge in edgeList:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)

# 7 16
# 5 3 18
# 1 2 21
# 2 6 25
# 0 2 31
# 0 1 32
# 3 4 34
# 5 4 40
# 2 4 46
# 0 6 51
# 4 6 51
# 0 5 60
# 5 3 18
# 1 2 21
# 2 6 25
# 0 2 31
# 3 4 34

# 175

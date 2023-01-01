# 행렬 덧셈

n, m = map(int, input().split())

map1 = list()
for i in range(n):
    map1.append(list(map(int, input().split())))

map2 = list()
for i in range(n):
    map2.append(list(map(int, input().split())))

ans = list()
for i in range(n):
    for j in range(m):
        ans.append(map1[i][j] + map2[i][j])

for i in range(1, len(ans) + 1):
    print(ans[i - 1], end=" ")
    if i % m == 0:
        print()

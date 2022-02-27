# 바닥장식
n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]

# 수평을 체크
def dfs_hori(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "-":
            graph[x][y] = "x"
            dfs_hori(x, y - 1)
            dfs_hori(x, y + 1)
            return
    else:
        return

# 수직을 체크
def dfS_vert(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "|":
            graph[x][y] = "x"
            dfS_vert(x - 1, y)
            dfS_vert(x + 1, y)
            return
    else:
        return

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "-":
            dfs_hori(i, j)
            cnt += 1
        elif graph[i][j] == "|":
            dfS_vert(i, j)
            cnt += 1

print(cnt)
# 음료수 얼려 먹기
n, m = map(int, input().split()) # 세로가 X축, 가로가 Y축

graph = [] # 초기화

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


ans = 0

for i in range(n): # X 축
    for j in range(m): # Y 축
        if dfs(i, j) == True:
            ans += 1


print(ans)

# 음료수 얼려 먹기
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

ans = 0

for i in range(N):
    for j in range(M):

        if dfs(i, j) == True:
            ans += 1

print(ans)
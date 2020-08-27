# 단지번호붙이기

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs (x, y):
    visited[x][y] = 1
    global nums

    if graph[x][y] == 1:
        nums += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)


numlist = []
nums = 0

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b)
            numlist.append(nums)
            nums = 0

print(len(numlist))

for n in sorted(numlist):
    print(n)
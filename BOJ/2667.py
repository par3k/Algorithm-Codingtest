# 단지번호붙이기

n = int(input())

graph = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[x][y] = True
    global nums

    if graph[x][y] == 1:
        nums += 1

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0<=new_x<n and 0<=new_y<n:
            if visited[new_x][new_y] == False and graph[new_x][new_y] == 1:
                dfs(new_x, new_y)

numlist = []
nums = 0

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and visited[a][b] == False:
            dfs(a, b)
            numlist.append(nums)
            nums = 0

print(len(numlist))


for n in sorted(numlist):
    print(n)


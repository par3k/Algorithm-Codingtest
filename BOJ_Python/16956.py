# 늑대와 양
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
flag = True


def make_fense():
    global flag
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'W':
                for dir in range(4):
                    nx, ny = i + dx[dir], j + dy[dir]
                    if 0 <= nx < r and 0 <= ny < c:
                        if graph[nx][ny] == '.':
                            graph[nx][ny] = 'D'
                        elif graph[nx][ny] == 'S':
                            flag = False


make_fense()
if not flag:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            print(graph[i][j], end='')
        print()
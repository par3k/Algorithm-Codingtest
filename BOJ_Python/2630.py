# 색종이 만들기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0


def cut_graph(x, y, t):
    global blue, white, graph
    color = graph[x][y]
    double_check = False
    for i in range(x, x + t):
        if double_check:
            break
        for j in range(y, y + t):
            if graph[i][j] != color:
                cut_graph(x, y, t//2)
                cut_graph(x + t//2, y, t//2)
                cut_graph(x, y + t//2, t//2)
                cut_graph(x + t//2, y + t//2, t//2)
                double_check = True
                break
    if not double_check:
        if graph[x][y] == 1:
            blue += 1
        else:
            white += 1


cut_graph(0, 0, n)
print(white)
print(blue)
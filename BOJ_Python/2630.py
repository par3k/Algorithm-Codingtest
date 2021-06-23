# 색종이 만들기
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000001)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0 # 답이 될 값들 지정


def solution(x, y, t):
    global w, b
    color = graph[x][y]
    flag = 0

    for i in range(x, x + t):
        if flag: break
        for j in range(y, y + t):
            if graph[i][j] != color:
                solution(x, y, t//2)
                solution(x + t//2, y, t//2)
                solution(x, y + t//2, t//2)
                solution(x + t//2, y + t//2, t//2)
                flag = 1
                break

    if not flag:
        if graph[x][y] == 1:
            b += 1
        else:
            w += 1


solution(0, 0, n)
print(w)
print(b)
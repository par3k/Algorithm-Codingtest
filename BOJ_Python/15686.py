# 치킨 배달
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans, home, chicken, tmp = int(1e9), list(), list(), list()


def solve(i, cnt):
    global ans
    if i > len(chicken):
        return
    if cnt == m:
        s = 0
        for hx, hy in home:
            dist = int(1e9)
            for j in tmp:
                cx, cy = chicken[j]
                dist = min(dist, abs(hx - cx) + abs(hy - cy))
            s += dist
        ans = min(ans, s)
        return
    tmp.append(i)
    solve(i + 1, cnt + 1)
    tmp.pop()
    solve(i + 1, cnt)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i + 1, j + 1))
        elif graph[i][j] == 2:
            chicken.append((i + 1, j + 1))
solve(0, 0)
print(ans)
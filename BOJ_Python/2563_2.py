import sys
input = lambda :sys.stdin.readline().rstrip()
graph = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if graph[i][j] == 1: continue
            graph[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            ans += 1

print(ans)
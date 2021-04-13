import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
visited = [0] * n


def dfs(start):
    visited[start] = 1
    for idx, j in enumerate(graph[start]):
        if j == 1 and not visited[idx]:
            visited[idx] = 1
            dfs(idx)


dfs(plan[0] - 1)
if 0 not in visited:
    print("YES")
    exit(0)

for i in plan:
    if visited[i - 1] == 0:
        print("NO")
        exit(0)
print("YES")

# 바이러스
n = int(input()) # 컴퓨터 수
c = int(input()) # 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)]

for _ in range(c):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com1].sort()
    graph[com2].append(com1)
    graph[com2].sort()

ans = 0
visited = [False] * (n + 1)

def dfs(depth):
    global ans
    visited[depth] = True
    for node in graph[depth]:
        if not visited[node]:
            dfs(node)
            ans += 1

dfs(1)
print(ans)
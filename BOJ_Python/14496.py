from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append(a)
    check[a] = 0
    while queue:
        node = queue.popleft()
        if node == b:
            return check[node]

        for i in graph[node]:
            if check[i] == -1:
                queue.append(i)
                check[i] = check[node] + 1
    return -1


a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    from_, to_ = map(int, input().split())
    if from_ == to_: continue
    graph[from_].append(to_)
    graph[to_].append(from_)

print(graph)
check = [-1] * (n + 1)
print(bfs(a, b))
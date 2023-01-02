# 최댓값

graph = [list(map(int, input().split())) for _ in range(9)]
max_val, x, y = 0, 0, 0

for i in range(9):
    for j in range(9):
        if graph[i][j] > max_val:
            max_val = max(graph[i][j], max_val)
            x, y = i, j

print(max_val)
print(x + 1, y + 1)
def dfs(x, y):
    # 매트릭스의 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재의 위치를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리를 해준다

        # 상, 하, 좌, 우의 위치를 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

cnt = 0
for a in range(n): # (0,0) 부터 (n, m) 까지 전체 탐색 시작
    for b in range(m):
        if dfs(a, b): # 현재의 위치에서 dfs를 실행해서 True가 되면,
            cnt += 1 # 카운트 + 1
print(cnt)


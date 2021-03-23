import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

tc = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    dp = [[1000000] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    dp[0][0] = graph[0][0]

    heap = list()
    heapq.heappush(heap, [graph[0][0], 0, 0])

    while heap:
        cost, x, y = heapq.heappop(heap)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + graph[nx][ny])
                heapq.heappush(heap, [dp[nx][ny], nx, ny])
                visited[nx][ny] = 1

    return dp[N - 1][N - 1]


while True:
    N = int(input())
    if N == 0: break
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs()
    print(f'Problem {tc}: {ans}')
    tc += 1
# 미로 만들기
import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

INF = sys.maxsize
dist = [[INF] * n for _ in range(n)]
heap = list()


def dijkstra():
    dist[0][0] = 0
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        cost, row, col = heapq.heappop(heap)

        if dist[row][col] < cost:
            continue

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            n_row = row + dx
            n_col = col + dy

            if 0 <= n_row < n and 0 <= n_col < n:
                n_cost = cost + arr[n_row][n_col]

                if n_cost < dist[n_row][n_col]:
                    heapq.heappush(heap, (n_cost, n_row, n_col))
                    dist[n_row][n_col] = n_cost


dijkstra()
print(dist[n-1][n-1])
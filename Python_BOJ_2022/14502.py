# 연구소
from collections import deque
import sys
sys.setrecursionlimit(100001)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp_graph = [[0] * m for _ in range(n)]

# 방향
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 안전지대를 카운트한다
def safeAreaCnt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 0:
                cnt += 1
    
    return cnt


# 바이러스가 퍼진다 - bfs
def spreadVirus(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

# 벽을 친다 - 재귀
ans = 0
def recursive(depth):
    global ans
    # 벽을 3개 세웠을 때
    if depth == 3:
        # 그 그래프를 임시 그래프에 복사해서
        for i in range(n):
            for j in range(m):
                tmp_graph[i][j] = graph[i][j]
        
        # 바이러스가 있는 자리에서 바이러스를 한번 퍼트려본다
        for i in range(n):
            for j in range(m):
                if tmp_graph[i][j] == 2:
                    spreadVirus(i, j)
        
        # 안전 지대의 갯수를 최댓값이 되도록 계속 업데이트
        ans = max(ans, safeAreaCnt())
        return

    # 빈공간에 한번 벽을 새워본다
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                depth += 1
                recursive(depth)
                graph[i][j] = 0
                depth -= 1

recursive(0)
print(ans)
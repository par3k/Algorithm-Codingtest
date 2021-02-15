# 2045 (Easy)
from collections import deque
from copy import deepcopy

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def move(board, di):
    visited = [[False] * n for _ in range(n)]

    if di in [0, 3]:
        start, end, step = 0, n, 1
    else:
        start, end, step = n-1, -1, -1

    for i in range(start, end, step):
        for j in range(start, end, step):
            if board[i][j] == 0: continue

            x, y = i, j
            val = board[x][y]
            board[x][y] = 0
            nx, ny = x + dx[di], y + dy[di]

            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n: break

                if board[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dx[di], y + dy[di]
                elif board[nx][ny] == val and not visited[nx][ny]:
                    x, y = nx, ny
                    visited[x][y] = True
                    break
                else:
                    break

            board[x][y] = board[x][y] + val
    return board


def bfs(board):
    queue = deque([board])
    max_val = -1
    step = 0

    while queue:
        for _ in range(len(queue)):
            board = queue.popleft()

            for di in range(4):
                n_board = move(deepcopy(board), di)
                queue.append(n_board)

                for i in range(n):
                    for j in range(n):
                        if n_board[i][j] > max_val:
                            max_val = n_board[i][j]

        step += 1
        if step == 5: # 스텝이 5회가 되면 강제 종료
            return max_val


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(bfs(arr))
# 사다리 조작
import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n, m, h = map(int, input().split())
board = [[False] * n for _ in range(h)]
if m == 0:
    print(0)
    exit(0)
for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = True


def checkBoard():
    for start in range(n):
        k = start
        for j in range(h):
            if board[j][k]:
                k += 1
            elif k > 0 and board[j][k - 1]:
                k -= 1
        if k != start: return False
    return True


def dfs(depth, x, y):
    global answer
    if checkBoard():
        answer = min(answer, depth)
        return
    elif depth == 3 or answer <= depth:
        return

    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0

        for j in range(k, n - 1):
            if not board[i][j] and not board[i][j + 1]:
                if j > 0 and board[i][j - 1]:
                    continue
                board[i][j] = True
                dfs(depth + 1, i, j + 2)
                board[i][j] = False


answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
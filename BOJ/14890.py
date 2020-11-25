# 경사로
import sys
input = lambda :sys.stdin.readline().rstrip()

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def check(arr):
    now_pos = arr[0]
    visited = [False for _ in range(n)]

    for row, height in enumerate(arr):

        if now_pos == height:
            continue # 높이가 같으면 그냥 진행

        elif now_pos + 1 == height: # 높은 곳으로 이동 할 떄, 남은 거리가 l보다 크거나 같으면 이동가능
            for j in range(row - 1, row - 1 - l, -1):
                if j < 0 or now_pos != arr[j] or visited[j]:
                    return False

                visited[j] = True
            now_pos = height

        elif now_pos - 1 == height: # 낮은 곳으로 이동 할 떄, 남은 거리가 l보다 크거나 같으면 이동가능
            for j in range(row, row + l):
                if j >= n or now_pos - 1 != arr[j] or visited[j]:
                    return False

                visited[j] = True
            now_pos = height

        else: # 높이 차이가 1 이상으로 나면 이동 불가
            return False

    return True


def solve():
    ans = 0
    for i in range(n):
        if check(graph[i]): # 1 row씩 체크
            ans += 1

    for j in range(n):
        col = list()
        for i in range(n):
            col.append(graph[i][j])

        if check(col): # 1 column씩 체크
            ans += 1

    print(ans)


solve()
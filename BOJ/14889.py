# 스타트와 링크
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split()))]
select = [0 for _ in range(n)]
ans = int(1e9)


def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += arr[i][j]

                elif not select[i] and not select[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]: continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


dfs(0, 0)
print(ans)
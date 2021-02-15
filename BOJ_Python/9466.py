# 팀 프로젝트
import sys
sys.setrecursionlimit(100001)
input = lambda: sys.stdin.readline().rstrip()


def dfs(n):
    global ans
    visited[n] = True
    loop.append(n)
    num = arr[n]

    if visited[num]:
        if num in loop:
            ans += loop[loop.index(num):]
        return
    else:
        dfs(num)


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    ans = list()

    for i in range(1, n + 1):
        if not visited[i]:
            loop = list()
            dfs(i)
    print(n - len(ans))


'''
3 1 3 7 3 4 6
'''
# 점프 점프

n = int(input())
arr = list(map(int, input().split()))
s = int(input()) - 1
visited = [False] * n
ans = 0
def dfs(x):
    global ans
    for nx in (x + arr[x], x - arr[x]):
        if 0 <= nx < n and not visited[nx]:
            ans += 1
            visited[nx] = True
            dfs(nx)

dfs(s)
print(ans)
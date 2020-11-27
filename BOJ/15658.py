import sys
sys.setrecursionlimit(100001)

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

max_val = -int(1e9)
min_val = int(1e9)


def dfs(idx, ans):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, ans)
        min_val = min(min_val, ans)
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(idx + 1, ans + arr[idx])
        op[0] += 1

    if op[1] > 0:
        op[1] -= 1
        dfs(idx + 1, ans - arr[idx])
        op[1] += 1

    if op[2] > 0:
        op[2] -= 1
        dfs(idx + 1, ans * arr[idx])
        op[2] += 1

    if op[3] > 0:
        op[3] -= 1
        dfs(idx + 1, int(ans / arr[idx]))
        op[3] += 1


dfs(1, arr[0])
print(max_val)
print(min_val)
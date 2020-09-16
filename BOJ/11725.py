import sys
sys.setrecursionlimit(10 ** 9)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(start, tree, ans):
    for i in tree[start]:
        if ans[i] == 0:
            ans[i] = start
            dfs(i, tree, ans)


dfs(1, tree, ans)

for i in range(2, n+1):
    print(ans[i])
# N과 M(1)
n, m = map(int, input().split())
chk = [False for _ in range(n + 1)]
ans = [0 for _ in range(m)]

def recursive(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        if chk[i]:
            continue
        ans[depth] = i
        chk[i] = True
        recursive(depth + 1)
        chk[i] = False

recursive(0)
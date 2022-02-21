# N과 M(2)
n, m = map(int, input().split())
ans = [0] * m

def recursive(depth, start):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    
    for i in range(start, n + 1):

        ans[depth] = i
        recursive(depth + 1, i + 1)


recursive(0, 1)
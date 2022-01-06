# N과 M(3)

n, m = map(int, input().split())

ans = [0] * (n + 1)

def combination(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        ans[depth] = i
        combination(depth + 1)

combination(0)
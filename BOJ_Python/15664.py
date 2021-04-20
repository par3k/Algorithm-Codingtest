# n과 m(10)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)
chk = [0] * (n + 1)


def Recursive(depth, start):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    overlap = 0
    for i in range(start, n):
        if chk[i]: continue
        if arr[i] != overlap:
            chk[i] = 1
            ans[depth] = arr[i]
            Recursive(depth+1, i + 1)
            overlap = arr[i]
            chk[i] = 0

Recursive(0, 0)
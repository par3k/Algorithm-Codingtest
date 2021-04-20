# n과 m (7)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)


def Recursive(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(n):
        ans[depth] = arr[i]
        Recursive(depth + 1)


Recursive(0)
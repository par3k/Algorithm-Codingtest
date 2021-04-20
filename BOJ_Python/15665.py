# n과 m (11)

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

    overlap = 0
    for i in range(n):
        if overlap == arr[i]: continue
        ans[depth] = arr[i]
        Recursive(depth + 1)
        overlap = arr[i]


Recursive(0)
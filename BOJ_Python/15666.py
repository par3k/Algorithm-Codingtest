# n과 m (12)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)


def Subset(depth, start):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    overlap = 0
    for i in range(start, n):
        if overlap != arr[i]:
            ans[depth] = arr[i]
            Subset(depth + 1, i)
            overlap = arr[i]


Subset(0, 0)
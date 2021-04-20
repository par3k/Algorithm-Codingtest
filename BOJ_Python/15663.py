# n과 m (9)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)
isUsed = [0] * (n + 1)


def Subset(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    overlap = 0
    for i in range(n):
        if isUsed[i]: continue
        elif overlap != arr[i]:
            isUsed[i] = 1
            ans[depth] = arr[i]
            overlap = arr[i]
            Subset(depth + 1)
            isUsed[i] = 0


Subset(0)
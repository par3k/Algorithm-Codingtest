# n과 m (9)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)
isused = [0] * (n + 1)


def Recursive(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(len(arr)):
        if isused[i]: continue
        isused[i] = 1
        ans[depth] = arr[i]
        Recursive(depth + 1)
        isused[i] = 0


Recursive(0)
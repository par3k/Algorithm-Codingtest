# N과 M(6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = [0] * (n + 1)


def Combination(depth, start):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return

    for i in range(start, len(arr)):
        ans[depth] = arr[i]
        Combination(depth + 1, i + 1)

Combination(0, 0)
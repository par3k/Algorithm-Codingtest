# N과 M

N, M = map(int, input().split())

check = [False] * (N + 1)
ans = [0] * M


def recursive(idx, n, m):
    if idx == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()

        return

    for i in range(1, n + 1):
        if check[i]:
            continue

        check[i] = True
        ans[idx] = i
        recursive(idx + 1, n, m)
        check[i] = False


recursive(0, N, M)
n = int(input())
first = list(map(int, input()))
second = list(map(int, input()))


def switch(a, b):
    tmp = a[:]
    cnt = 0
    for i in range(1, n):
        if tmp[i-1] == b[i-1]:
            continue
        cnt += 1

        for j in range(i-1, i+2):
            if j < n:
                tmp[j] = 1 - tmp[j]
    return cnt if tmp == b else float('inf')


result = switch(first, second)
first[0] = 1 - first[0]
first[1] = 1 - first[1]

result = min(result, 1 + switch(first, second))
print(result if result != float('inf') else -1)
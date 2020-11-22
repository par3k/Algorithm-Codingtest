# 가장 긴 팰린드롬 부분 문자열 - 못 품

s = list(input())
n = len(s)

s += [0 for _ in range(200000)]
r = [0 for _ in range(200000)]

for i in range(2 * n - 2, -1, -1):
    if i % 2 == 0:
        s[i] = s[i / 2]
    else:
        s[i] = '#'

ans = 0
p = rmax = -1
n = 2 * n - 1

for i in range(n):
    if i <= rmax:
        r[i] = min(rmax - i, r[2 * p - i])
    j = r[i] + 1
    while i - j > 0 and i + j < n:
        if s[i - j] == s[i + j]:
            r[i] += 1
        else:
            break
        j += 1
    if rmax < i + r[i]:
        p = i
        rmax = p + r[p]

for i in range(n):
    if i % 2 == 0:
        if r[i] / 2 * 2 + 1 > ans:
            ans = r[i] / 2 * 2 + 1
        else:
            if (r[i] + 1) / 2 * 2 > ans:
                ans = (r[i] + 1) / 2 * 2
print(ans)
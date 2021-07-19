# 야바위 대장

s = list(map(str, input()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]
print(''.join(s))
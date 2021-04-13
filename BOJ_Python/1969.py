import sys
input = lambda :sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
alphabet = [[0] * 26 for _ in range(m)]


for i in range(m):
    for j in range(n):
        alphabet[i][ord(arr[j][i]) - ord('A')] += 1

s = ''
for i in range(m):
    max = -123456789
    idx = 0
    for j in range(26):
        if alphabet[i][j] > max:
            max = alphabet[i][j]
            idx = j
    s += chr(idx + ord('A'))

print(s)

ans = 0
for i in range(n):
    for j in range(m):
        if (s[j] != arr[i][j]):
            ans += 1
print(ans)
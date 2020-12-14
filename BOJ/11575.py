# Affine Chipher
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a, b = map(int, input().split())
    s, ans = input(), list()
    for i in range(len(s)):
        ans.append(chr(((a * (ord(s[i]) - ord('A')) + b) % 26) + ord('A')))
    print(''.join(ans))
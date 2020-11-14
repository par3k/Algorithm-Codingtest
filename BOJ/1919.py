# 애너그램 만들기
import sys
input = lambda :sys.stdin.readline().rstrip()

in_a, in_b = list(input()), list(input())
a = [0 for _ in range(26)]
b = [0 for _ in range(26)]

ans = 0

for i in range(0, len(in_a)): a[ord(in_a[i]) - 97] += 1
for i in range(0, len(in_b)): b[ord(in_b[i]) - 97] += 1
for i in range(26):
    if a[i] != b[i]: ans += abs(a[i] - b[i])

print(ans)
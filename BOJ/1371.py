# 가장 많은 글자
import sys

n = sys.stdin.read()
alpha = [0 for i in range(26)]

for s in n:
    if s.islower():
        alpha[ord(s) - 97] += 1

for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(i + 97), end='')
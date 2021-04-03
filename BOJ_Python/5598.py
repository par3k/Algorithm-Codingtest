# 카이사르 암호
import sys
s = list(map(str, sys.stdin.readline().rstrip()))

for i in range(len(s)):
    asciii = ord(s[i]) - ord('A') - 3
    if asciii < 0:
        asciii += 26
    print(chr(asciii + ord('A')), end='')

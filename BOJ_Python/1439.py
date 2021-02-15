# 뒤집기
import sys
input = lambda :sys.stdin.readline().rstrip()
s = list(input())

convert_1, convert_0 = 0, 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i-1] == '0':
            convert_1 += 1
        else:
            convert_0 += 1

if s[-1] == '0':
    convert_1 += 1
else:
    convert_0 += 1

print(min(convert_1, convert_0))
# 파일 완전 삭제
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
s, d = list(map(str, input())), list(map(str, input()))

for i in range(n):
    for j in range(len(s)):
        if s[j] == '1':
            s[j] = '0'
        elif s[j] == '0':
            s[j] = '1'

if s == d:
    print("Deletion succeeded")
else:
    print('Deletion failed')
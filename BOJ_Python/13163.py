# 닉네임에 갓 붙이기
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(input().split())
    s[0] = 'god'
    print(''.join(s))

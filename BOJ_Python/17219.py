# 비밀번호 찾기
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = dict(input().split() for _ in range(n))

for _ in range(m):
    site = input()
    print(arr.get(site))
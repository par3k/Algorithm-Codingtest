# 수 정렬하기
import sys

input = lambda : sys.stdin.readline().rstrip()

ans = sorted([int(input()) for i in range(int(input()))])
print(*ans, sep='\n')
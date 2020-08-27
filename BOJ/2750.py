# 수 정렬하기

import sys

ans = sorted([int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))])
print(*ans, sep='\n')
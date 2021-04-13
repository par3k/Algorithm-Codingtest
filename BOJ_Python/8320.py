# 직사각형을 만드는 방법
import sys
n = int(sys.stdin.readline().rstrip())
ans = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if i * j <= n:
            ans += 1
print(ans)
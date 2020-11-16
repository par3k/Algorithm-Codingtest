# 이상한 곱셈
import sys
input = lambda :sys.stdin.readline().rstrip()

a, b = map(str, input().split())
a_tmp, b_tmp = 0, 0

for i in range(len(a)):
    a_tmp += int(a[i])
for j in range(len(b)):
    b_tmp += int(b[j])

print(a_tmp * b_tmp)

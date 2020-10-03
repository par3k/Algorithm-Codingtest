# 나는 위대한 슈퍼스타 K
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
arr = dict()

for i in range(m):
    put = input().split()
    for i in range(0, len(put), 2):
        arr[int(put[i])] = max(float(put[i+1]), arr.get(int(put[i]), 0))

print("%.1f" %sum(e for e in sorted(list(arr.values()), reverse=True)[0:k]))
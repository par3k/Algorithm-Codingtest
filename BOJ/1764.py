# 듣보잡
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dut = set([input() for _ in range(n)])
bo = set([input() for _ in range(m)])
tmp = dut & bo
ans = list(tmp)
ans.sort()

print(len(ans))
for i in ans: print(i)
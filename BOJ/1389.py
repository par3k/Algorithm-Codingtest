# 케빈 베이컨의 6단계 법칙 - 플로이드 워셜 알고리즘
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
table = [[n for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1
    table[b-1][a-1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                table[i][j] = 0
            else:
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

ans = list()
for i in table:
    ans.append(sum(i))
print(ans.index(min(ans)) + 1)
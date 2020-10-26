# 도서관
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
books = list(map(int, input().split()))

plus, minus = list(), list()
for i in range(n):
    if books[i] >= 0:
        plus.append(books[i])
    else:
        minus.append(books[i])

plus = sorted(plus, reverse=True)

for i in range(len(minus)):
    minus[i] = minus[i] * -1
minus = sorted(minus, reverse=True)

idx, result, M = 0, 0, 0
while idx < len(plus):
    if plus[idx] > M:
        result += plus[idx]
        result += M
        M = plus[idx]
    else:
        result += plus[idx] * 2
    idx += m

idx = 0
while idx < len(minus):
    if minus[idx] > M:
        result += minus[idx]
        result += M
        M = minus[idx]
    else:
        result += minus[idx] * 2
    idx += m

print(result)
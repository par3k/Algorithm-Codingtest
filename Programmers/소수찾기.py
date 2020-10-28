import math

n = int(input())

is_Prime = [True] * (n+1)
max_length = math.ceil(math.sqrt(n))
ans = []

for i in range(2, max_length):
    if is_Prime[i]:
        for j in range(i + i, n+1, i):
            is_Prime[j] = False

for i in range(2, n+1):
    if is_Prime[i]:
        ans.append(i)

print(len(ans))
# 통계학

import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])

avg = round(sum(arr) / n)
range = max(arr) - min(arr)

tmp = len(arr) // 2
mid = arr[tmp]


print(avg)
print(mid)
if n == 1:
    print(arr[0])
else:
    most = Counter(arr).most_common(2)
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
print(int(range))
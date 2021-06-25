# 반전 요세푸스
from collections import deque

N, K, M = map(int, input().split())
arr = deque(i + 1 for i in range(N))

ans = []
i = -(K - 1)
flag = False

while arr:
    if len(ans) % M == 0 and len(ans) >= M and not flag:
        flag = True
        i = K
    elif len(ans) % M == 0 and len(ans) >= M and flag:
        flag = False
        i = -(K - 1)
    arr.rotate(i)
    ans.append(arr.popleft())

print("\n".join(map(str, ans)))
# 풍선 터뜨리기
from collections import deque
n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, num = q.popleft()
    ans.append(idx + 1)
    if num > 0:
        q.rotate(-(num-1))
    elif num < 0:
        q.rotate(-num)

print(' '.join(map(str, ans)))
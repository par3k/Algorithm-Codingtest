# 빈도 정렬
import sys
input = lambda :sys.stdin.readline().rstrip()

n, c = map(int, input().split())
arr = list(map(int, input().split()))
cnt = {}

for i in range(n):
    if arr[i] in cnt:
        cnt[arr[i]][0] += 1
    else:
        cnt[arr[i]] = [1, i]
print(cnt)
res = sorted(cnt.items(), key=lambda x: (-x[1][0], x[1][1]))
ans = []
for i in res:
    for j in range(i[1][0]):
        ans.append(str(i[0]))
print(' '.join(ans))
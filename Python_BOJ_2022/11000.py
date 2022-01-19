# 강의실 배정
import heapq

n = int(input())
timeTable = list()
for i in range(n):
    start, end = map(int, input().split())
    timeTable.append([start, end])

timeTable.sort()

cnt, ans = 0, 0
tmp = list()

for i in range(n):
    cnt += 1
    heapq.heappush(tmp, timeTable[i][1])
    while timeTable[i][0] >= tmp[0]:
        cnt -= 1
        heapq.heappop(tmp)
    ans = max(ans, cnt)

print(ans)

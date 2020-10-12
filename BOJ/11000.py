# 강의실 배정
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(a, key=lambda x: x[0])

queue = list()
heapq.heappush(queue, arr[0][1])

for c in arr[1:]:
    if c[0] >= queue[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, c[1])

print(len(queue))
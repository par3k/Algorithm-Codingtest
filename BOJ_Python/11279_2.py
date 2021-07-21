# 최대 힙
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
    s = int(input())
    if s == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-s, s])

# N번째 큰수
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
heap = []
for _ in range(n):
    s = list(map(int, input().split()))
    if len(heap) == 0:
        for i in s:
            heapq.heappush(heap, i)
    else:
        for i in s:
            if heap[0] < i:
                heapq.heappush(heap, i)
                heapq.heappop(heap)

print(heap[0])
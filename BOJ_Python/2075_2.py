# N번째 큰 수
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

heap = []
n = int(input())

for _ in range(n):
    s = list(map(int, input().split()))
    if not len(heap):
        for i in s:
            heapq.heappush(heap, i)
    else:
        for i in s:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heapq.heappop(heap))
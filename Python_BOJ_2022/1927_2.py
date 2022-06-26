# 최소 힙
import heapq

arr = list()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, n)
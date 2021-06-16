import heapq

arr = []
heapq.heappush(arr, 1)
heapq.heappush(arr, 10)
heapq.heappush(arr, 2)
heapq.heappush(arr, 9)
heapq.heappush(arr, 4)
heapq.heappush(arr, 5)
print(arr)

while arr:
    print(heapq.heappop(arr))
# 절댓값 힙
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

arr = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(a), a))
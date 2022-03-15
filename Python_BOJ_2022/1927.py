# 최소 힙
import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

arr = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, num)
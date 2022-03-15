# 최대 힙
import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

arr = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if len(arr):
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (-num, num))
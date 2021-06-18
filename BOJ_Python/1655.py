# 가운데를 말해요
import heapq, sys
input = lambda :sys.stdin.readline().rstrip()

min, max = [], []
for _ in range(int(input())):
    a = int(input())
    if len(max) == len(min):
        heapq.heappush(max, (-a, a))
    else:
        heapq.heappush(min, (a, a))

    if len(max) >= 1 and len(min) >= 1 and max[0][1] > min[0][1]:
        max_val, min_val = heapq.heappop(max)[1], heapq.heappop(min)[1]
        heapq.heappush(max, (-max_val, max_val))
        heapq.heappush(min, (min_val, min_val))
    print(max[0][1])

# arr, tmp = [], []
# for _ in range(int(input())):
#     a = int(input())
#     heapq.heappush(arr, a) # 힙으로 저장
#
#     if len(arr) == 1: # 1개면 중간값은 자기 자신
#         print(arr[0])
#     else:
#         while len(arr):
#             tmp.append(heapq.heappop(arr))
#
#         for i in tmp:
#             arr.append(i)
#         tmp = []
#
#         if len(arr) % 2 != 0:
#             print(arr[len(arr) // 2])
#         else:
#             print(arr[(len(arr) // 2) - 1])

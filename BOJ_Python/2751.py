# 수 정렬하기 퀵솔트도 시간초과
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
#
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[0]
#     tail = arr[1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
#
# print(*quick_sort(arr), sep='\n')

import sys

ans = sorted([int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))])
print(*ans, sep='\n')
# 나무 자르기
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
tree = list(map(int, input().split()))

result = 0

def binary_search(arr, target, start, end):
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in arr:
            if x > mid:
                total += x - mid

        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


print(binary_search(tree, m, 0, max(tree)))
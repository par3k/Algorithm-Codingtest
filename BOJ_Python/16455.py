# import heapq
# def kth(a, k):
#     heap = []
#     for i in a:
#         heapq.heappush(heap, i)
#
#     cnt = 0
#     ans = 0
#     while cnt < k:
#         ans = heapq.heappop(heap)
#         cnt += 1
#     return ans

def kth(a, k):
    target = k - 1
    start = 0
    end = len(a) - 1

    while True:
        i, j = start, end

        while True:
            while i <= end and a[i] <= a[start]:
                i += 1
            while a[j] > a[start]:
                j -= 1
            if i >= j: break
            a[i], a[j] = a[j], a[i]
        a[start], a[j] = a[j], a[start]
        if j == target:
            return a[j]
        elif j < target:
            start = j + 1
        else:
            end = j - 1



arr = [3,1,4,5,2]
print(kth(arr, 2))
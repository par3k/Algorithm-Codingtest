# 파이썬 문법 사용시 단축되는 퀵 솔트

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
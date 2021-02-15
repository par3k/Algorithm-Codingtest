'''
# 이진탐색(binary search)
탐색 범위를 절반씩 줄여나가면서 찾는다
Youtube : https://www.youtube.com/watch?v=Q8uUOMY5Hec&list=PLAdQRRy4vtQRwAGymS3q3VXk1WUfhZg7l&index=19

# 장점
1. 빠르다 O(log n)
2. 실제로 쓰인다.

# 단점
1. 정렬이 되어 있어야 한다.
2. 만들기 어렵다.

# 핵심로직
중간 인덱스값을 구한다.
10억 -> 5억
5억 -> 2.5억
범위가 절반씩 줄어든다.
'''
arr = [1,2,3,5,6,7,8,9,10,11]


def binarySearch(arr, targetNumber):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        midIndex = (start + end) // 2
        print(midIndex, arr[midIndex])

        if arr[midIndex] > targetNumber:
            end = midIndex - 1
        elif arr[midIndex] < targetNumber:
            start = midIndex + 1
        else:
            print()
            return midIndex
    return -1


print('result : ',binarySearch(arr, 8))
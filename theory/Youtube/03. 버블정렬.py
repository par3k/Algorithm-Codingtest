'''
알고리즘에서 가장 첫번째로 나오는 알고리즘
거품이 물에서 떠오르는 모양

핵심로직 :
첫번째거랑 두번째꺼랑 비교해서 두번째께 더 작으면 첫번째거랑 자리를 바꾼다.
'''

arr  = [6, 5, 4, 3, 2, 1]
print(arr)

def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr

print('결과 : ', bubbleSort(arr))
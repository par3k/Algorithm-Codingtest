import heapq

def heapsort(arr):
    h, result = list(), list()
    for i in arr:
        heapq.heappush(h, -i)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 2, 9, 4, 8 ,6, 0])
print(result)


# 힙 자료구조는 데이터를 힙에 넣었다가 꺼내기만 해도 정렬이 된다.
# O(N log N) 의 Time Complexity 보장
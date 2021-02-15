'''
단순탐색(Simple Search)
* 앞에서부터 원하는게 나올 때까지 하나하나 찾는다

장점
1. 만들기 쉽다.
2. 정렬이 안되어 있어도 된다

단점
1. 느리다.
2. 10억개를 탐색할때, 최대 10억번 연산 O(n)

대안
* 이진탐색(Binary Search) O(log n)
'''
#Q.8은 몇번째에 있을까?

arr = [1,2,3,5,6,7,8,9,10,11]
def simpleSearch(arr, targetNum):
    for index in range(0, len(arr)):
        if targetNum == arr[index]:
            return index
    return -1


print(simpleSearch(arr, 8))
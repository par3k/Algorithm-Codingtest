from itertools import permutations
import math

numbers = '17'


def Eratosthenes(n): # 에라토스테네스의 체로 소수 리스트 제작
    flag = [True for _ in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if flag[i] == True:
            j = 2
            while i * j <= n:
                flag[i * j] = False
                j += 1

    return [i for i in range(2, n + 1) if flag[i]]


def solution(numbers):
    tmp = []
    for i in range(1, len(numbers) + 1):
        tmp += list(map(''.join, permutations(numbers,i)))

    arr = []
    for i in range(len(tmp)):
        arr.append(int(tmp[i]))
    arr = list(map(int, set(arr)))

    answer = 0
    prime_number = Eratosthenes(max(arr))
    for i in range(len(arr)):
        if arr[i] in prime_number:
            answer += 1

    return answer


print(solution(numbers))
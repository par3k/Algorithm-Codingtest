## Day 3

# def recursive_sum(n):
#     print(n)
#     if n <= 1:
#         return n
#     else:
#         return n+sum(n-1)
#
# a = int(input('Write the Number : '))
# print(recursive_sum(a))

'''
만약 if로 1 이하의 경우를 브레이크 걸지 않으면 음수까지 계속 진행함
'''

# def iteration_sum(n):
#     sum = 0
#     while n >= 0:
#         print(n)
#         sum += n
#         n -= 1
#
#     return sum
#
# a = int(input('Write the Number : '))
# print(iteration_sum(a))

'''
둘다 복잡도는 O(n)으로 같으나
Efficiency는 Recursive가 더 좋다.
'''

# def sum(n):
#     return n*(n+1) // 2
#
# a = int(input('Write the Number : '))
# print(sum(a))

'''
이 방법이 O(1)로 가장 빠름
'''

# def factorial(n):
#     print(n)
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# a = int(input('Write the Number : '))
# print(factorial(a))


# def fibonacci(n):
#     result = 0
#     F0 = 0
#     F1 = 1
#     if n == 0:
#         result = F0
#     elif n == 1:
#         result = F1
#     elif n > 1:
#         result = fibonacci(n-1) + fibonacci(n-2)
#     return result
#
# a = int(input('Write the Number : '))
# print(fibonacci(a))

# def iteration_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         i = 2
#         t0 = 0
#         t1 = 1
#
#         while i <= n:
#             t0, t1 = t1, t0+t1
#             i += 1
#     return t1
#
# a = int(input('Write the Number : '))
# print(iteration_fibonacci(a))

'''
피보나치의 수열 또한 재귀함수로 구현이 가능하다
'''

# def factorial(n):
#
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# def combi(n, m):
#     return factorial(n) / (factorial(b) * factorial(n-m))
#
# a = int(input('Write the Number1 : '))
# b = int(input('Write the Number2 : '))
# print(combi(a, b))

'''
조합의 수 계산도 재귀함수로 구현이 가능하다
위의 문제 : n개의 서로 다른 원소에서 m개를 택하는 경우의 
'''

def solution(L, x, start, end):
    if end < start:
        return -1

    mid = (start + end)//2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, start, mid-1)
    else:
        return solution(L, x, mid+1, end)

L = [4, 9, 16, 25, 36, 49, 64, 81]
x = int(input('Find num : '))
start = int(input('From : '))
end = int(input('To : '))
print('The result idx is', solution(L, x, start, end))

'''
리스트 L과, 그 안에서 찾으려는 원소 x가 인자로 주어지고,
또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l부터 u까지로 정해질 때,
x와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution()을 완성하시오.

만약 리스트 L 안에서 x와 같은 값을 가지는 원소가 존재하지 않을 경우에는 -1을 리턴합니다.
리스트 L은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정한다.
또한, 동일한 원소는 2번 이상 나타나지 않습니다.

인덱스 범위를 나타내는 l과 u가 인자로 주어지는 이유는, 이 함수를 재귀적인 방법으로
구현하기 위함입니다.

빈 칸에 알맞은 내용을 채워서 재귀 함수인 solution()을 완성하세요.
'''
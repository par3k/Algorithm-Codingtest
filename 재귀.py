# def sum(n):
#     print(n)
#     if n <= 1:
#         return n
#     else:
#         return n + sum(n-1)
#
# n = int(input())
# print('result : ', sum(n))

# def pac(n):
#     print(n, end=' ')
#     if n <= 1:
#         return 1
#     else:
#         return n * pac(n-1)
#
# n = int(input())
# print('>> result : ', pac(n))

# def recursive(n):
#     sum = 0
#     F0 = 0
#     F1 = 1
#     if n == 0:
#         sum = F0
#     elif n == 1:
#         sum = F1
#     elif n > 1:
#         sum = recursive(n-1) + recursive(n-2)
#     return  sum
#
# n = int(input())
# print(recursive(n))

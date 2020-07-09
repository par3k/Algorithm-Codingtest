## Day 1

# L = ['Bob', 'Steve', 'Sap']
# print(L)
# print(type(L))
#
# L.append('New')
# print(L)
#
# L.pop()
# print(L)

# K = [20, 37, 45, 72, 96, 102]
# print(K)
# K.insert(3, 99)
# print(K)
# del(K[2])
# print(K)

# L = ['Bob', 'Steve', 'Sap']
# print(L.index('Sap'))
#
# for i in range(len(L)):
#     print(L[i], end=' ')

# def solution(L, x):
#     for i in range(len(L)-1):
#         if L[i] <= x:
#             if x <= L[i+1]:
#                 L.insert(i+1, x)
#                 break
#         else:
#             L.insert(0, x)
#             break
#     answer = L
#     return L
#
# L = [2, 3, 6, 9, 16, 25, 36, 49, 64, 81, 100]
# x = int(input('X value : '))
# print(solution(L, x))

def solution(L, x):
    idx = []
    for i in range(len(L)):
        if L[i] == x:
            idx.append(i)
            if len(idx) == 0:
                idx.append(-1)
            return idx

L = [4, 9, 16, 25, 36, 49, 64, 81]
x = int(input('X value : '))
print(solution(L, x))
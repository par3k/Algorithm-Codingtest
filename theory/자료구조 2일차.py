## Day 2

# L = [3, 8, 2, 16, 1, 49]
# L.sort()
# print(L)

# L.sort(reverse=1)
# print(L)

# def linear_search(L, x): # O(n)
#     i = 0
#     while i < len(L) and L[i] != x:
#         i += 1
#     if i < len(L):
#         return i
#     else:
#         return -1
#
# L = [3, 8, 2, 16, 1, 49]
# x = int(input('X value : '))
# print(linear_search(L, x))

def binary_search(L, x): # O(logn)
    lower = 0
    upper = len(L)-1
    idx = -1

    while lower <= upper:
        middle = (lower + upper)//2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1

    return idx

L = [3, 8, 2, 16, 1, 49]
x = int(input('X value : '))
print(binary_search(L, x))
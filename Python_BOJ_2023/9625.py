# BABBA

k = int(input())

# 0 -> [1, 0]
# 1 -> [0, 1]
# 2 -> [1, 1]
# 3 -> [1, 2]
# 4 -> [2, 3]
# 5 -> babbabab [3, 5]
# 6 -> babbababbabba [5, 8]
# 7 -> babbababbabbababbabab [8, 13]

arr = [[1, 0], [0, 1], [1, 1]]

if k >= 3:
    for i in range(3, k + 1):
        arr.append([arr[i - 2][0] + arr[i - 1][0], arr[i - 2][1] + arr[i - 1][1]])

print(arr[k][0], arr[k][1])
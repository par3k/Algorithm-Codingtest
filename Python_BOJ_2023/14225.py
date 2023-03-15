# 부분수열의 합

n = int(input())
arr = list(map(int, input().split()))

list = [0] * 20000000

def dfs(depth, num):
    if depth == n:
        list[num] = 1
        return
    dfs(depth + 1, num)
    dfs(depth + 1, num + arr[depth])

dfs(0, 0)

for i in range(len(list)):
    if list[i] == 0:
        print(i)
        break
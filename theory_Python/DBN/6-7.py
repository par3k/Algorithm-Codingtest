# 두 배열의 원소 교체

N, K = map(int, input().split())


arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

arr_1.sort()
arr_2.sort(reverse=True)


for j in range(K):
    if arr_1[j] < arr_2[j]:
        arr_1[j], arr_2[j] = arr_2[j], arr_1[j]
    else: break


print(sum(arr_1))
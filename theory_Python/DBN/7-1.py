# 순차 탐색


def seq_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1


print("생성할 원소 갯수를 입력한 다음 한 칸 띄고 문자열을 입력하세요.")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 갯수만큼 문자열을 입력하세요.")
arr = input().split()

print(seq_search(n, target, arr))
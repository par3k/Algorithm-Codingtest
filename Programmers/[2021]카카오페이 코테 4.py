ages = [35, 25, 3, 8, 7]
wires = [[1, 2, 5], [2, 1, 5], [1, 3, 2], [3, 4, 2], [3, 5, 20], [4, 5, 1]]


def solution(ages, wires):
    maxWireLength = [0] * (len(ages) + 1)
    for i in wires:
        start, end, length = i[0], i[1], i[2]
        maxWireLength[end] = max(maxWireLength[end], length + ages[start - 1])

    arr = [0] * len(ages)
    for i in range(len(ages)):
        arr[i] = [i + 1, min(ages[i], maxWireLength[i + 1])]
    arr.sort(key = lambda x: x[1])

    answer = []
    for i in range(len(arr)):
        answer.append(arr[i][0])
    return answer


print(solution(ages, wires))
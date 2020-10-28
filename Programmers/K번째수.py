array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    tmp = []
    for i in range(len(commands)):
        for j in range(commands[i][0]-1, commands[i][1]):
            tmp.append(array[j])
            tmp.sort()
        answer.append(tmp[commands[i][2] - 1])
        tmp = []

    return answer


print(solution(array, commands))
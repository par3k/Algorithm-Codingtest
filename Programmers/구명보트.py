# people = [70, 50, 80, 50]
people = [70, 80, 50]
limit = 100


def solution(people, limit):
    answer = []
    flag = False

    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            if people[i] + people[j] > limit:
                continue
            else:
                answer.append([people[i], people[j]])
                flag = True

        if flag:
            flag = False
            continue
        else:
            answer.append(people[i])
    print(answer)
    return answer

solution(people, limit)
n = int(18372)


def solution(n):
    answer = ''
    for i in sorted(str(n), reverse=True):
        answer += i
    return int(answer)
print(solution(n))
brown, yellow = 24, 24


def solution(brown, yellow):
    answer = [0, 0]
    sum = brown + yellow
    a = 1
    while True:
        a += 1
        b = sum // a

        if a >= b and a * b == sum:
            if (a - 2) * (b - 2) == yellow:
                answer[0], answer[1] = a, b
                break

    return answer


print(solution(brown, yellow))
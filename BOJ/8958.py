# OX 퀴즈

n = int(input())

quiz = []
for i in range(n):
    quiz = list(input())

    cnt = 0
    sum = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            cnt += 1
            sum += cnt
        elif quiz[i] == 'X':
            cnt = 0
            sum += cnt

    print(sum)
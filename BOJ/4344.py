# 평균은 넘겠지

C = int(input())

test_case = []
for i in range(C):
    test_case = list(map(int, input().split()))
    sum = 0
    avg = 0
    count = 0
    # print(test_case)

    for j in range(1, len(test_case)):
        sum += test_case[j]
        avg = sum / test_case[0]
    # print(int(avg))

    for k in range(1, len(test_case)):
        if test_case[k] > int(avg):
            count = count + 1
    # print(count)
    
    people = count / test_case[0] * 100
    print("%.3f%%" %people)
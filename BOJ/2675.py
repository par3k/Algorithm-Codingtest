# 문자열 반복

T = int(input())

for i in range(T):
    R, S = input().split(' ')
    R = int(R)
    S = list(S)

    memory = []
    for j in range(len(S)):
        for k in range(R):
            memory.append(S[j])

    print(str.join('', memory))
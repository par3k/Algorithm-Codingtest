n, k = map(int, input().split())
girl = [0] *  1000
boy = [0] * 1000

for i in range(n):
    sex, grade = map(int, input().split()) # sex > 0 : 여자, 1 : 남자
    if sex == 0:
        girl[grade] += 1
    else:
        boy[grade] += 1

for i in range(1, 7):
    if girl[i] % k == 0:
        girl[i] = girl[i] // k
    else:
        girl[i] = girl[i] // k + 1

    if boy[i] % k == 0:
        boy[i] = boy[i] // k
    else:
        boy[i] = boy[i] // k + 1

ans = sum(girl) + sum(boy)
print(ans)
# 뚊
n, m = map(int, input().split())

answer = []
for _ in range(n):
    sentence = input()
    answer.append(sentence)
answer.sort()

compare = []
for _ in range(n):
    sentence2 = input()
    compare.append(sentence2)
compare.sort()

flag = False
for i in range(n):
    tmp = ''
    for j in answer[i]:
        tmp += j * 2

    if tmp != compare[i]:
        print("Not Eyfa")
        exit(0)

print("Eyfa")
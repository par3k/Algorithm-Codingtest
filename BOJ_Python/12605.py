# 단어순서 뒤집기
num = int(input())
answer = list()

for i in range(num):
    N = list(input().split(' '))
    reversed = N[::-1]
    answer.append(' '.join(reversed))

for i in range(num):
    print("Case #{0}: {1}".format(i+1, answer[i]))
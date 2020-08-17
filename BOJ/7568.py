# 덩치

T = int(input())

people = []

for _ in range(1, T+1):
    w, h = map(int, input().split())
    people.append((w, h))


for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')


'''
5
55 185
58 183
88 186
60 175
46 155
'''
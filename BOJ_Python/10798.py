# 세로읽기
tmp = []
max_len = 0

for _ in range(5):
    word = input()
    tmp.append(list(word))

    if len(word) > max_len:
        max_len = len(word)

answer = ''
i = 0

while i < max_len:
    for j in range(5):
        if len(tmp[j]) != 0:
            answer += tmp[j].pop(0)
    i += 1

print(answer)
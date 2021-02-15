# 단어 정렬

N = int(input())
words = [input() for _ in range(N)]
words = sorted(words, key=lambda x: (len(x), x))

tmp = ''

for i in words:
    if tmp != i:
        print(i)
        tmp = i
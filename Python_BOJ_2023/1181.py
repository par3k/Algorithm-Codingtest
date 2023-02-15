# 단어 정렬

n = int(input())
words = list(input() for _ in range(n))
words = sorted(words, key= lambda x: (len(x), x))
print(words)
tmp = ''
for i in words:
    if tmp != i:
        print(i)
        tmp = i
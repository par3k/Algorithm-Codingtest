# 단어 공부

S = input().upper()

index = []

for i in range(26):
    index.append(0)

for j in range(26):
    index[j] = S.count(chr(j+ord('A')))

if index.count(max(index)) > 1:
    print('?')
else:
    print(chr(index.index(max(index))+ord('A')))
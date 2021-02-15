# 그룹 단어 체커

n = int(input())
ans = []

for i in range(n):
    word = list(str(input()))

    for j in range(len((word))):
        if j != len(word)-1 and word[j] == word[j+1]:
            pass
        elif word[j+1:].count(word[j]) != 0:
            break
        elif j == len(word)-1:
            ans.append(i)
print(len(ans))
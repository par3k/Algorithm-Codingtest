# 서로 다른 부분 문자열
s = input()
answer = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[i: j + 1]
        answer.add(tmp)
print(len(answer))
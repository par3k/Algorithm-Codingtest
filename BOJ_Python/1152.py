# 단어의 개수
'''
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문자열

단어는 띄어쓰기 한개로 구분됨

공백이 연속으로 나오는 경우는 없다

문자열의 앞과 뒤에는 공백이 있을 수도 있다.
'''

n = input()

count = 1

for i in range(0, len(n)):
    search = n[i]

    if i == 0 or i == len(n) - 1 and search == ' ':
        continue
    elif search == ' ':
        count += 1

if len(n) == 1 and search == ' ':
    count = 0

print(count)
# 모음의 갯수
import sys
mo = ['a', 'e', 'i', 'o', 'u']
cnt = 0

while True:
    sentence = list(map(str, sys.stdin.readline().rstrip().lower()))
    if sentence == ['#']: break
    for i in range(len(sentence)):
        if sentence[i] in mo:
            cnt += 1
    print(cnt)
    cnt = 0
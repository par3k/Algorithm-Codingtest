# 연길이의 이상형
import sys
mbti = list(map(str, sys.stdin.readline().rstrip()))

for i in range(4):
    if mbti[i] == "E":
        mbti[i] = "I"
    elif mbti[i] == "I":
        mbti[i] = "E"
    elif mbti[i] == "S":
        mbti[i] = "N"
    elif mbti[i] == "N":
        mbti[i] = "S"
    elif mbti[i] == "T":
        mbti[i] = "F"
    elif mbti[i] == "F":
        mbti[i] = "T"
    elif mbti[i] == "J":
        mbti[i] = "P"
    else:
        mbti[i] = "J"

print(''.join(mbti))
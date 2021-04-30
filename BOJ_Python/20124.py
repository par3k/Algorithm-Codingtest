# 모르고리즘 회장님 추천 받습니다.
import sys
input = lambda : sys.stdin.readline().rstrip()

max = 0
ans = ''

for i in range(int(input())):
    name, score = input().split()
    if int(score) > max:
        max = int(score)
        ans = name

    elif int(score) == max:
        if name < ans:
            max = int(score)
            ans = name

print(ans)
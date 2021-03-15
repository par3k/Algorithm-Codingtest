# 숫자 야구
from itertools import permutations

n = int(input())
arr =[0 for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

result = 0

def sol(x):
    cnt= 0
    for i in range(n):
        strike = 0
        ball_arr = set()
        ball = 0
        for j in range(3):
            if str(x)[j] == str(arr[i][0])[j]:
                strike += 1
            ball_arr.add(str(x)[j])
            ball_arr.add(str(arr[i][0])[j])
        ball = 6 - len(ball_arr) - strike
        if strike == arr[i][1] and ball == arr[i][2]:
            cnt += 1
    if cnt == n:
        return True


for i in permutations(range(1, 10), 3):
    num = 0
    for j in range(3):
        num += i[j] * 10 ** j
    if sol(num) is True:
        result += 1

print(result)

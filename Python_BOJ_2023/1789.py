# 수들의 합

s = int(input())

sum_val = 0
answer = 0

while True:
    answer += 1
    sum_val += answer
    if sum_val > s:
        break

print(answer - 1)

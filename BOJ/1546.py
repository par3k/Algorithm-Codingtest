n = int(input())
score = list(map(int, input().split()))

M = max(score)

new_list = []
sum = 0

for i in range(n):
    new_avg = score[i] / M * 100
    new_list.append(new_avg)
    sum = new_list[i] + sum

avg = sum / n

print(avg)


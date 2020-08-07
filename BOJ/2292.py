# 벌집

n = int(input())
round = 1

while n > 1:
    n = n - ( 6 * round)
    round += 1

print(round)


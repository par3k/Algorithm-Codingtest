# 상근날드

hambug = []
drink = []

for i in range(5):
    a = int(input())

    if i < 3:
        hambug.append(a)
    else:
        drink.append(a)

print(min(hambug) + min(drink) - 50)
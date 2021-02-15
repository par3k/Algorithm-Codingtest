# 여우는 어떻게 울지?
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    animal_sounds = list(input().split())

    sounds = list()
    while True:
        animal = list(input().split())
        if len(animal) > 3:
            break
        sounds.append(animal[2])

    for s in sounds:
        ans = list()
        for i in animal_sounds:
            if i != s:
                ans.append(i)
        animal_sounds = ans

    print(*ans)
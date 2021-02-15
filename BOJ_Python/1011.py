# fly me to the Alpha Centauri
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    x, y = map(int, input().split())

    lr = y - x
    cnt = 1

    while True:
        if cnt ** 2 <= lr < (cnt + 1) ** 2:
            break
        cnt += 1

    if cnt ** 2 == lr:
        print(cnt * 2 - 1)
    elif cnt ** 2 < lr <= cnt ** 2 + cnt:
        print(cnt * 2)
    else:
        print(cnt * 2 + 1)
        
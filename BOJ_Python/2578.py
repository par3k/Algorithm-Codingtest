import sys
input = lambda :sys.stdin.readline().rstrip()

bingo = [list(map(int, input().split())) for _ in range(5)]
tmp = [list(map(int, input().split())) for _ in range(5)]
cmd = list()
for i in range(5):
    for j in range(5):
        cmd.append(tmp[i][j])


def find_bingo():
    total = 0
    for i in range(5):
        cnt1 = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt1 += 1
                if cnt1 == 5:
                    total += 1
    for i in range(5):
        cnt2 = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt2 += 1
                if cnt2 == 5:
                    total += 1
    cnt3 = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt3 += 1
            if cnt3 == 5:
                total += 1
    cnt4 = 0
    for i in range(5):
        if bingo[i][4 - i] == 0:
            cnt4 += 1
            if cnt4 == 5:
                total += 1
    return total


cnt = 0
for k in range(len(cmd)):
    cnt += 1
    for i in range(5):
        for j in range(5):
            if cmd[k] == bingo[i][j]:
                bingo[i][j] = 0
                if find_bingo() >= 3:
                    print(cnt)
                    exit(0)



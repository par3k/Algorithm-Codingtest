# 주사위 쌓기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]

# A B C D E F 일때,
# A F
# B D
# C E 가 주사위 위 아래 짝이된다.

route = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
max_ans = 0
for i in range(6):
    ans = list()

    tmp = [1, 2, 3, 4, 5, 6]
    tmp.remove(dice[0][i])

    next = dice[0][route[i]]

    tmp.remove(next)
    ans.append(max(tmp))

    for j in range(1, n):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(next)

        next = dice[j][route[dice[j].index(next)]]

        tmp.remove(next)
        ans.append(max(tmp))

    ans = sum(ans)

    if max_ans < ans:
        max_ans = ans

print(max_ans)
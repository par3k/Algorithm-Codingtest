# 한조서열정리하고옴ㅋㅋ
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
group = list(map(int, input().split()))

kill_cnt = 0
max_kill = 0
ans = 0


for i in group:
    if i > max_kill:
        max_kill = i
        kill_cnt = 0
    else:
        kill_cnt += 1
    ans = max(ans, kill_cnt)

print(ans)
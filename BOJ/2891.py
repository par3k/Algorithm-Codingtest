# 카약과 강풍
import sys
input = lambda : sys.stdin.readline().rstrip()

n, s, r = map(int, input().split())

damage_team = list(map(int, input().split()))
spare_team = list(map(int, input().split()))
team = [1 for _ in range(n+1)]

for i in range(s): team[damage_team[i]-1] -= 1
for j in range(r): team[spare_team[j]-1] += 1
for k in range(n):
    if team[k] == 0:
        if k == 0 and team[1] == 2:
            team[1] -= 1
            team[0] += 1
        elif k == n and team[k-1] == 2:
            team[k-1] -= 1
            team[k] += 1
        else:
            if team[k-1] == 2:
                team[k-1] -= 1
                team[k] += 1
            elif team[k+1] == 2:
                team[k+1] -= 1
                team[k] += 1

print(team.count(0))